a = [1,2,3]
b = ['abc','def','ghi']
t = list(zip(a,b))
print(t)


for j in map(lambda x,y : (x,y),a,b):
    print(j)




