def f(x):
    if(x%100 ==0):
        if(x%400 ==0):
            return 1
    elif(x%4 == 0):
        return 1
    else : return 0
	
print(list(filter(f,[2012,2016,2015,2001,2000,2100])))
