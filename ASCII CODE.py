a=input('enter string to find ASCII code  ')
print('ASCII code of '+str(a)+'\tis')
for i in a:
    print(i,end=' ')
    print(ord(i),end=' ')




# To convert ASCII codes to chars(reverse)
n=int(input("enter size  "))
a=[int(input("enter value"))for i in range(0,n)]
for i in a:
    print(chr(i),end='')
for i in a:
    print(a,end='')