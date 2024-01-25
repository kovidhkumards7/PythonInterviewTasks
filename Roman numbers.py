a=int(input('enter value <5000  '))
b=[]
if(a<5000):
    while (a>0):
        if (a>=1000):
            b.append('M')
            a=a-1000
        elif (a>=500):
            b.append('D')
            a=a-500
        elif (a>=100):
            b.append('C')
            a=a-100
        elif (a>=50):
            b.append('L')
            a=a-50
        elif (a>=10):
            b.append('X')
            a = a - 10
        elif (a>=5):
            b.append('V')
            a=a-5
        elif (a>=1):
            b.append('I')
            a=a-1
else:
    print('invalid number')
for i in b:
    print(i,end='\t')
