import math
a=[]
b=str((input('enter binary sequence  ')))
a.extend(b)
d=0
for i in range(0,len(a)):
    if (int(a[i])==0) or (int(a[i])==1):
        d=d+1
if (d==len(a)):
    c=[]
    c=a[::-1]
    s=0
    for i in range(0,len(c)):
        s=s+(int(c[i])*math.pow(2,i))
    print(s)
else:
    print("this is not a binary code")