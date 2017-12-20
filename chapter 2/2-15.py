filename = raw_input("input file name:")
fobj = open(filename,'r')
print "fobj***********",fobj
for eachLine in fobj:
	print eachLine,
fobj.close()