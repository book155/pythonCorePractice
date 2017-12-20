import keyword
idenfy= raw_input()


if len(idenfy)==1:
    print "idetify lenth is 1" 

if idenfy in (keyword.kwlist):
    print "you input is keywork !!!!!!"
