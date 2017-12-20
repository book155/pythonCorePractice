print "please input 1-100:"
input = raw_input()
num = int(input)
while 1==1 :
	if (num > 1 and num<100) :
		print "this is ok : %d" % num
		break
	else :
		print "please input 1-100 again:"
		input = raw_input()
		num = int(input)
