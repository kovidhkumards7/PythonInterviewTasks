a=int(input('enter number  '))
b=[]
while a>0:
    b.append(a%2)
    a=int(a/2)
c=b[::-1]
for i in c:
    print(i,end=' ')