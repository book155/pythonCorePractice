import moneyfmt
#print type(moneyfmt)
cash = moneyfmt.MoneyFmt(123.45)
print cash.update(1)
print cash
print cash.dollarize(123456.8901)
print cash.dollarize(-123456.8901)
print cash.__nonzero__()









print 'test dir()'
print "module dir---------------------------"
print dir(moneyfmt)
print "class.object dir------------------------"
print dir(cash)
print cash.__str__
print cash.__dict__
print "class dir---------------------"
print cash.__dirClass__()
print help(moneyfmt)
