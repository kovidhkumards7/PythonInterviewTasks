import math
a=int(input('enter an positive integer value  '))
n=len(str(a))
print('lenght of the given string is  '+str(n))
print('the input number is  '+str(a))
print('type of the input number is  ')
print(type(a))
t=a
s=0
for i in range(0,n,1):
    d=t%10
    s=s+math.pow(d,n)
    t//=10
print('the amstrong number came up to be  '+str(s))
if(s==a):
    print('given integer is an amstrong number')
else:
    print('given integer is not an amstrong number')