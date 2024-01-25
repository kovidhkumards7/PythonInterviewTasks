# PGRM TO FIND THE VALUE OF EULER'S FORMULAE (e) UPTO A CERTAIN ACCURACY
n=int(input('enter the accuracy value( should be greater than 1 )  '))
sum=0
b=1
if(n>1):
    while (b<n+1):
        f=1
        for i in range(1,b):
            f=float(f*i)
        sum=float(sum+(1/f))
        b=b+1
    print('the value of e with accuracy upto '+str(n)+' is ',round(sum,25))
else:
    print("invalid range")
print(type(sum))
print(type(f))
print(type(b))