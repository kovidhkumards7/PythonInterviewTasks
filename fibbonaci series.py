n=int(input('enter the no of terms  '))
a=0
b=1
d=[0,1]
for i in range(2,n,1):
    c=a+b
    a=b
    b=c
    d.append(c)
print(d)




# fibonacci btw a range of user entered numbers
a = int( input( "enter lower level  " ) )
b = int( input( "enter upper level  " ) )
c = [ 0 , 1 ]
x , y ,z = 0 , 1 , 0

while ( z < ( b + 1 ) ):
    z = x + y
    c.append( z )
    x = y
    y = z
for i in range( 0 , len( c ) ):
    if ( c[ i ] >= a ) and ( c[ i ] < b ):
        print( c[ i ] , end = " " )