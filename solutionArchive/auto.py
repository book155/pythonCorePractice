# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import time
import re
import json
import configparser
archivePath = os.getcwd() + os.sep + 'archive'
configFile = os.getcwd() + os.sep + 'config.ini'
curTime = time.time()
allList = []
import sys
import codecs

#获取一个领域的归档的时间
def getDomainArchiveTime(domain_dirname):
    orginalTimeList= []
    filelist = os.listdir(archivePath + os.sep + domain_dirname)
    if not filelist:
        return '',''
    for file in filelist:
        originalTime = os.path.getmtime(archivePath + os.sep + domain_dirname + os.sep + file)
        orginalTimeList.append(originalTime)
    difTime = curTime - max(orginalTimeList)
    difHour = round(difTime / 3600,1)
    standardTime = time.strftime('%m-%d %H:%M',time.localtime(max(orginalTimeList)))
    return difHour,standardTime

#获取领域CIE和PM信息
def getDomainArchver(domain_dirname):
    f = codecs.open(configFile, "r", "utf-8")
    config = configparser.ConfigParser()
    config.readfp(f)
    try:str_CIEandPM = config.get("CIEandPM",domain_dirname)
    except configparser.NoOptionError:
        return ' , '
    if len(str_CIEandPM.split(',')) == 1: return str_CIEandPM + ', '
    else: return str_CIEandPM

#输入2-NETWORK 输出NETWORK
def getDomain(domain_dirname):
    return re.match('\d+-(\w+)',domain_dirname).group(1)

def myMain():
    domainList = os.listdir(archivePath)
    for domain_dirname in domainList:
        if not os.path.isfile(archivePath + os.sep + domain_dirname):
            #目录名称必须满足数字-领域名的格式
            if re.match('\d+-.*',domain_dirname) is not None:
                dict = {}
                domainPath = archivePath + os.sep + domain_dirname
                dict["domain"]=getDomain(domain_dirname)
                arcivetime = getDomainArchiveTime(domain_dirname)
                dict["timeDifToNow"]=arcivetime[0]
                dict["achiveTime"]=arcivetime[1]
                list_CIEandPM = getDomainArchver(domain_dirname).split(',')
                dict["achiver"]= list_CIEandPM[0]
                dict["PM/PL"]= list_CIEandPM[1]
                allList.append(dict)
    new_json = json.dumps(allList,sort_keys=True, indent=5)
    #print allList
    #f = open('allList.json','w')
    #f.write(new_json)
    return allList
    
