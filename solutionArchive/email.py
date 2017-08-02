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
    tableTitle_str = config.get("email","tableTitle").split(',')
    body.append("{0:.<13} {1:.<11} {2:.<13} {3:.<18} {4:.<11} {5:.<15}".format(tableTitle_str[0],tableTitle_str[1],tableTitle_str[2],tableTitle_str[3],tableTitle_str[4],tableTitle_str[5]))
    for newLine in listNews:
        tableContent = "{0:.<15} {1:.<15} {2:.<15} {3:.<15} {4:.<15} {5:.<15}".format(newLine['domain'], newLine['achiveTime'],newLine['achiver'],newLine['PM/PL'],newLine['timeDifToNow'],newLine['vmpStatus'])
        body.append(tableContent)
    body.append(os.linesep)
    body.append(os.linesep)
    body.append(config.get("email","content"))
    print(body)
    f = open('body.json','w')
    f.write(str(body))
    mail.Body = '\r\n'.join(body)
    mail.Send()
    print("send ok")
      
if __name__ =="__main__":
    listNews = auto.myMain()
    outlook(listNews)
    