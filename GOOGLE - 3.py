# GOOGLE CODE - 3 for initializing values in 2 lists and asking the user to enter a value, to find out that the sum of any 2
# elements from each list makes it equal to the value or not. If equal,print true once else print false once:
# u tube link  =  https://youtu.be/sfuZzBLPcx4
m=int(input("enter size of 1st array  "))
n=int(input("enter size of 2nd array  "))
print("enter values of 1st list")
a=[int(input()) for i in range(0,m)]
print("enter values of 2nd list")
b=[int(input()) for i in range(0,n)]
c=[]
v=int(input("enter the sum value  "))
print("The entered lists are  ",a,'  ',b)
for i in range(0,m):
    for j in range(0,n):
        if(v==(a[i]+b[j])):
            c.append("true")
        else:
            c.append("false")
d=0
for i in c:
    if(i=='true'):
        d=1
        break
    else:
        d=0
if(d==1):
    print("true")
else:
    print("false")