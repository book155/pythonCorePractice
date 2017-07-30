#!/usr/bin/env python
# -*- coding: utf-8 -*-
import win32com.client as win32
import auto
import os
import sys
import ConfigParser

reload(sys)
sys.setdefaultencoding('utf-8')
configFile = os.getcwd() + os.sep + 'config.ini'

def outlook(listNews):
    f = open(configFile,'r')
    config = ConfigParser.ConfigParser()
    config.readfp(f)
    body = []
    app= 'Outlook'
    olook = win32.gencache.EnsureDispatch("%s.Application" % app)    
    mail=olook.CreateItem(win32.constants.olMailItem)
    substr = 'achive new List'.encode('utf-8')
    subj = mail.Subject = substr.decode('utf-8')
    receiver = config.get("email","receiver")
    for receiverOne in receiver.split(','):
        mail.Recipients.Add(receiverOne)
    body.append(config.get("email","emailContent") + os.linesep)
    tableTitle = 'domain'.ljust(20) + 'achiveTime'.ljust(20) +'achiver'.ljust(20) + 'PM/PL'.ljust(20) + 'timeDifToNow'.ljust(20) + os.linesep
    body.append(tableTitle)
    for newLine in listNews:
        content = newLine['domain'].ljust(20) + newLine['achiveTime'].ljust(20) + newLine['achiver'].ljust(20) + newLine['PM/PL'].ljust(20) + str(newLine['timeDifToNow'])  + os.linesep
        body.append(content)
    print body
    mail.Body = '\r\n'.join(body)
    mail.Send()
    print "send ok"
      
if __name__ =="__main__":
    listNews = auto.myMain()
    outlook(listNews)
    