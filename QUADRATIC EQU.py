import math
a=float(input('enter value  '))
b=float(input('enter value  '))
c=float(input('enter value  '))
if(a!=0):
    d=float(math.sqrt((math.pow(b,2))-(4*a*c)))
    x=float(((-b)+d)/(2*a))
    y=float(((-b)-d)/(2*a))
    print('roots are '+str(x)+'  '+str(y))