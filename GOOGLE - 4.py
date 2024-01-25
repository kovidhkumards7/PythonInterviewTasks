# GOOGLE CODE - 4 for asking the user to input an array of integers, write a pgrm to find the maximun value of sum
# of any 2 integers in the array list
n=int(input("enter size of array  "))
print("enter values of list")
a=[int(input()) for i in range(0,n)]
b=[]
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            continue
        else:
            b.append(int(a[i]+a[j]))
s=0
for i in range(0,len(b)):
    if(b[i]>s):
        s=b[i]
print("the greatest of sum of 2 integers in a list is  ",s)


a.sort()
print(a[-2]+a[-1])