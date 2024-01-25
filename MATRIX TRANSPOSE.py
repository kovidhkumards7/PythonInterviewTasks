# TRANSPOSE of an MATRIX
m1=int(input('enter no of rows in A '))
n1=int(input('enter no of cols in A '))
print('enter element of mat A')
a=[[int(input()) for i in range(n1)] for j in range(m1)]
print('Matrix A is :')
for i in range(m1):
    for j in range(n1):
        print(a[i][j], end='    ')
    print()
print('Transpose matrix is :')
for i in range(n1):
    for j in range(m1):
        print(a[j][i],end="     ")
    print()