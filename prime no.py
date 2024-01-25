a=int(input('enter the number  '))
if(a==0 or a==1):
    print('its prime')
elif(a>1):
    for i in range(2,a,1):
        if (a%i)==0:
            b=1
            break
        else:
            b=0
if(b==0):
    print('prime')
else:
    print('not prime')



