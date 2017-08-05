def countToFour1():
    for eachNum in range(5):
        print(eachNum)
def countToFour2(n):
    for eachNum in range(n,5):
        print(eachNum)
def countToFour3(n=1):
    for eachNum in range(n,5):
        print(eachNum)
#EROOR
#countToFour1(2)

#2,3,4
countToFour2(2)
#2,3,4
countToFour3(2)

#ERROR
#countToFour1(4)
#4
countToFour2(4)
#4
countToFour3(4)

#ERROR
#countToFour1(5)
#NONE
print(type(countToFour2(5)))
#NONE
print(type(countToFour3(5)))

#0,1,2,3,4
countToFour1()
#ERROR
#countToFour2()
#1,2,3,4
countToFour3()
