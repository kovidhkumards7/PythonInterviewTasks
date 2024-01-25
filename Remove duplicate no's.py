a=[]
n=int(input('enter size  '))
for i in range(0,n):
    a.append(int(input('enter the value  ')))
print('the entered list is  \n'+str(a))
print('after removal of duplicate elements....')
print(list(dict.fromkeys(a)))


a=[]
n=int(input('enter size  '))
for i in range(0,n):
    a.append(int(input('enter the value  ')))
b=[]
c=-1
for i in a:
    if i not in b:
        b.append(i)
        c+=1
    else:
        c+=1
        print("the duplicate value is "+str(i)+" present at "+str(c))
print('the entered list is  \n'+str(a))
print('after removal of duplicate elements....')
print(b)

a={2,6,26,5,2,265,5,656,596,496,2,496}
print(a)