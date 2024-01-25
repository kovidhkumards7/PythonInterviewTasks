a=int(input('enter number  '))
b=[]
for i in range(1,a):
    if (a%i==0):
        b.append(i)
s=0
for i in b:
    s=s+int(i)
if(a==s):
    print("it's a perfect number")
else:
    print("it's not a perfect number")