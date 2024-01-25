print('To find the number of vowels in a sentence')
a=input("enter a sentence  ")
s=0
b=[]
for i in range(0,len(a)):
    if (a[i]=='a') or (a[i]=='e') or (a[i]=='i') or (a[i]=='o') or (a[i]=='u') or (a[i]=='A') or (a[i]=='E') or (a[i]=='I') or (a[i]=='O') or (a[i]=='U'):
        b.append(a[i])
        s=s+1
print(s)
print('they are',end=" ")
for i in b:
    print(i,end=" ")