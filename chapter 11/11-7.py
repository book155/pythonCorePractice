a = [1,2,3]
b = ['abc','def','ghi']
#t = list(zip(a,b))
#print(t)

def f(x,y):
    print('def f:')
    return (x,y)
#map= [(1,'abc'),(2,'def'),(3,'ghi')]
for j in map(f,a,b):
    print(j)




