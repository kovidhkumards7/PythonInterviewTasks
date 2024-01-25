print("MATRIX RAISED TO A POWER")
m=int(input('enter no of rows in A '))
n=int(input('enter no of cols in A '))
if(m==n):
    print("enter matrix elements")
    a=[[int(input())for i in range(n)]for j in range(m)]
    n=int(input("enter the power value to be raised  "))
    b=[[0 for i in range(n)]for j in range(m)]
    while(n>0):
        for i in range(m):
            for j in range(n):
                for k in range(m):
                    b[i][j]=b[i][j]+(a[i][k]*a[k][j])
        n=n-1
    print("the powered matrix is")
    for i in range(m):
        for j in range(n):
            print(b[i][j],end="     ")
        print()
else:
    print("invalid size")