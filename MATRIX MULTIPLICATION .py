print('to execute A*B matrix multiplication')
m1=int(input('enter no of rows in A '))
n1=int(input('enter no of cols in A '))
m2=int(input('enter no of rows in B '))
n2=int(input('enter no of cols in B '))
if(n1==m2):
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
    c=[[0 for i in range(m1)]for j in range(n2)]
    for i in range(m1):
        for j in range(n2):
            for k in range(m2):
                c[i][j]=c[i][j]+(a[i][k]*b[k][j])
    print("the multiplied matrix is")
    for i in range(m1):
        for j in range(n2):
            print(c[i][j],end="     ")
        print()
else:
    print('invalid sizes of matrices, matrices multiplication is not possible')