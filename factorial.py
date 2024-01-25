n=int(input('enter the no of terms  '))
p=1
while n>0:
    p=(p*n)
    n=n-1
print(p)
for i in range(1,n+1,1):
    p=p*i
print(p)