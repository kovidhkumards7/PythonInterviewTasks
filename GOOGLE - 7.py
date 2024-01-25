#  GOOGLE CODE - 7 for finding the largest consecutive number in the array list
#  u tube link  -  https://youtu.be/TgCKJU3JvO4
n=int(input("enter size of the list  "))
a=[int(input("enter value  ")) for i in range(0,n)]
a.sort()
b=[]
c=0
for i in range(0,n-1):
    c=i+1
    if((a[i]+1)==a[c]):
        b.append(a[i])
e=b[-1]+1
b.append(e)
print(b)



