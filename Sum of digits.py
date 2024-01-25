print("To find sum of digits")
a=int(input("enter the number"))
s=0
d=0
t=a
while(a>0):
    d=a%10
    s=s+d
    a//=10
print(s)