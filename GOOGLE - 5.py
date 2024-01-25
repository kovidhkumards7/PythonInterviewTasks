# GOOGLE CODE - 5 for finding the sorted squared list for the user entered list
# u tube link  =  https://youtu.be/4eWKHLSRHPY
import math
n=int(input("enter size of array  "))
print("enter values of list")
def s(n):
    a=[int(input()) for i in range(0,n)]
    b=[math.pow(i,2) for i in a]
    b.sort()
    print(b)
s(n)