#!/usr/bin/env python
# -*- coding: utf-8 -*-
import win32com.client as win32
import auto
import os
import sys
import configparser
import codecs

configFile = os.getcwd() + os.sep + 'config.ini'
leftdiff = 20
char='.'
def outlook(listNews):
    f = codecs.open(configFile, "r", "utf-8")
    config = configparser.ConfigParser()
    config.readfp(f)
    body = []
    app= 'Outlook'
    olook = win32.gencache.EnsureDispatch("%s.Application" % app)    
    mail=olook.CreateItem(win32.constants.olMailItem)
    mail.Subject = config.get("email","emailTitle")
    for receiverOne in config.get("email","receiver").split(','):
        mail.Recipients.Add(receiverOne)
    body.append(config.get("email","emailContent"))
    body.append(os.linesep)
    body.append(config.get("email","tableTitle"))
    for newLine in listNews:
        content = newLine['domain'].ljust(leftdiff-5,char) + newLine['achiveTime'].ljust(leftdiff,char) + newLine['achiver'].ljust(leftdiff,char) + newLine['PM/PL'].ljust(leftdiff,char) + str(newLine['timeDifToNow'])
        body.append(content)
    body.append(os.linesep)
    body.append(os.linesep)
    body.append(config.get("email","content"))
   # print(body)
    f = open('body.json','w')
    f.write(str(body))
    mail.Body = '\r\n'.join(body)
  #  mail.Send()
    print("send ok")
      
if __name__ =="__main__":
    listNews = auto.myMain()
    outlook(listNews)
    