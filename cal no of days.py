print('enter DOB')
d=int(input('enter the date  '))
m=int(input('enter the month number  '))
y=int(input('enter the year  '))
print('Note - your age is been calculated as on 20-04-2020(dd-mm-yyyy)')
d1=20
m1=4
y1=2020
if (d1>=d):
    days=d1-d
else:
    m1=m1-1
    days=d1-d+30
if (m1>=m):
    months=m1-m
else:
    y1=y1-1
    months=m1-m+12
if (y1>=y):
    years=y1-y
else:
    print('entered value incorrect')
print("It's been "+str(days)+" days "+str(months)+" months "+str(years)+" years")
ty=0
for i in range(y,y1+1):
    if(i%4==0):
        ty=ty+366
    else:
        ty=ty+365
if(y%4==0):
    mlist=[31,29,31,30,31,30,31,31,30,31,30,31]
else:
    mlist=[31,28,31,30,31,30,31,31,30,31,30,31]
tm=0
for i in range(0,months+1):
    tm=tm+mlist[i]
td=ty+tm+days
print('total days are '+str(td))









