a=int(input('enter starting range  '))
b=int(input('enter ending range  '))
n=0
for i in range(a,b+1,1):
    if(i%2==0):
        print(i)
        n+=1
print("we have encountered "+str(n)+" even numbers")


a=int(input('enter starting range  '))
b=int(input('enter ending range  '))
n=0
for i in range(a,b+1,1):
    if(i%2!=0):
        print(i)
        n+=1
print("we have encountered "+str(n)+" odd numbers")