a=input('enter something  ')
try:
    b=int(a)
except:
    b=0
print(a)
print(b)


import cmath
a=float(input("enter the real part  "))
b=float(input("enter the imaginary part  "))
c=complex(a,b)
print(c.real)
print(c.imag)
print(c)


a=complex(input('enter a number  '))
print(type(a))
print(a.real)
print(a.imag)