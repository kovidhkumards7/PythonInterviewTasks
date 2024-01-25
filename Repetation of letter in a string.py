a=input("enter string  ")
b=[]
c={}
b.extend(a)
for i in b:
    c[i]=c.get(i,0)+1
print(c)