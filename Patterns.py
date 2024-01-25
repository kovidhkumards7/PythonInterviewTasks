# a=int(input('enter number  '))
# c=" "
# d="*"
# e=a
# print((c*a),(d))
# for i in range(1,a+1):
#     print((c*e),(d*i*2))
#     e=e-1
#
# a=int(input('enter number  '))
# b="*"
# c=" "
# d=a
# for i in range(1,a+1):
#     print((c*i),(b*d*2),(c*i))
#     d=d-1
# print((c*i),(b))
#
#
# a=[]
# n=int(input("enter size  "))
# for i in range(0,n):
#     a.append(int(input("enter value  ")))
# b=1
# for i in range(0,n):
#     print(str(a[i])*b)
#     b=b+1
#
# n=int(input('enter size >2  '))
# a='*'
# b=' '
# if (n>2):
#     print(a)
#     print(a,a)
#     for i in range(0,n-1):
#         print(a,(b*i),a)
#     print(a*(n+2))
# else:
#     print('invalid range')
#
# n=int(input('enter the size  '))
# a='*'
# b=' '
# c='* *'
# print(a*(n+4))
# while((n+1)>0):
#     print(a,b*n,a)
#     n=n-1
# print(c)
# print(a*2)
# print(a)
#
# a=[]
# a.extend('python')
# b=1
# for i in range(0,len(a)):
#     print(a[i]*b)
#     b=b+1
#
# # EQUILATERAL TRIANGLE
# n=int(input('enter no  '))
# a='*'
# b=' '
# c=n
# print((b*(c+1)),(a))
# for i in range(1,n):
#     print((b*c),(a*i*2),(b*c),end='\n')
#     c=c-1
#
#
# a = input( "enter the string " )
# n = 1
# while ( n < len( a ) + 1 ):
#     for i in range( 0 , n ):
#         print( a[i] , end = "" )
#     print()
#     n+=1
#
#
# a = input( "enter a number  ")
# n = int( a )
# while ( n > 0 ):
#     print( n*str(n))
#     n=n-1