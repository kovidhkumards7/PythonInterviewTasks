a=int(input('enter number  '))
t=a
s=''
while (t>0):
    d=t%10
    s=s+str(d)
    t//=10
print(s)


