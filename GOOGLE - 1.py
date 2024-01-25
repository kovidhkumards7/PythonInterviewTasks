# GOOGLE CODE - 1 for printing the least indexing difference of a integer in a list being repeated
# u tube link  =  https://youtu.be/XSdr_O-XVRQ
a=[]
n=int(input('enter size  '))
for i in range(0,n):
    a.append(int(input('enter value  ')))
print('the entered values are ',a)
b=[]
for i in range(0,n):
    for j in range(i+1,n):
        if(a[i]==a[j]):
            b.append((j-i))
print("the list of repeated indexes are  ",b)
s=none
for i in b:
    if(i<s):
        s=i
print("the duplication at the least difference of indexing is  ",s)