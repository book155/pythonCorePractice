#去除每行排头和最位的空白
import re
#def fileClear(f):
#
#    regex2 ='^'+str(chr(32))+'+|'+str(chr(32))+'+$'
#    strALL = ''
#    for eachLine in f:
#        stringnew = re.sub(regex2,'',eachLine)
#        strALL = strALL + stringnew
#    f.close()
#    return strALL
#
#
#f = open('11-11.txt','r')
#strALL = fileClear(f)
#print('Y-NewFile,N-OldFile,please input Y or N:')
#input = input()
#if input == 'Y':
#    file = open('11-11_new.txt', 'w')
#elif input == 'N':
#    file = open('11-11.txt','w')
#file.write(strALL)
#

def convert(x,y):
    regex2 ='^'+str(chr(32))+'+|'+str(chr(32))+'+$'
    y = re.sub(regex2,'',x)
    return x,y

file = open('11-11.txt','r')
list1 = []
list2 = []
strALL = ''

for eachLine in file:
    list1.append(eachLine)
    list2.append('')
for j in map(convert,list1,list2):
        strALL = strALL + j[1]

print('Y-NewFile,N-OldFile,please input Y or N:')
input = input()
if input == 'Y':
    file_new = open('11-11_new.txt', 'w')
elif input == 'N':
    file_new = open('11-11.txt','w')
file_new.write(strALL)