# to find perfect numbers in btw a range
a=int(input('enter lower limit  '))
b=int(input('enter upper limit  '))
print("the perfect numbers in between raange "+str(a)+" and "+str(b)+" are")
for i in range(a,b+1):
    sum=0
    for n in range(1,i):
        if (i%n==0):
            sum=sum+n
    if(i==sum):
        print(sum)