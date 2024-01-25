# ADDITION and SUBTRACTION of 2 2 dimentional arrays
m1=int(input('enter no of rows in A '))
n1=int(input('enter no of cols in A '))
m2=int(input('enter no of rows in B '))
n2=int(input('enter no of cols in B '))
if(n1==n2) and (m1==m2):
    print('enter element of mat A')
    a = [[int(input()) for i in range(n1)] for j in range(m1)]
    print('Matrix A is :')
    for i in range(m1):
        for j in range(n1):
            print(a[i][j], end='    ')
        print()
    print('enter element of mat B')
    b = [[int(input()) for i in range(n2)] for j in range(m2)]
    print('Matrix B is :')
    for i in range(m2):
        for j in range(n2):
            print(b[i][j], end='    ')
        print()
    print('Matrix A+B is :')
    for i in range(m1):
        for j in range(n1):
            print(a[i][j]+b[i][j],end='    ')
        print()
    print('Matrix A-B is :')
    for i in range(m1):
        for j in range(n1):
            print(a[i][j]-b[i][j],end='    ')
        print()
else:
    print("invalid sizes, matrices can't be operated")