
def sumT() :
	print 1+2+100
def avgT() :
	print (1+2+100)/3

	
print "please input 1,2 or X"
print "************************"
print "1 mean sum"
print "2 mean avg"
print "x mean exit"
print "************************"
input = raw_input()
if input == "1" :
	sumT()
elif input == "2" :
	avgT()
elif input == "X" :
	exit()
else :
	print "input error"
