# GOOGLE CODE - 8 for declaring 2 lists of elements, checking and printing a element if it's present in the first list
# but not in second list
m = int(input("enter size of 1st array  "))
n = int(input("enter size of 2nd array  "))
a = [input("enter the elementof 1st list  ")for i in range(0,m)]
b = [input("enter the elementof 2nd list  ")for i in range(0,n)]
c = []
for i in a:
    if i not in b:
        c.append(i)
print("the elements present in 1st list and not present in 2nd list are :")
print(c)


m = int(input("enter size of 1st array  "))
n = int(input("enter size of 2nd array  "))
a = [input("enter the elementof 1st list  ")for i in range(0,m)]
b = [input("enter the elementof 2nd list  ")for i in range(0,n)]
dict = {}
for i in a:
    dict[i] = dict.get(i,0)
for i in b:
    dict[i] = dict.get(i,0)+1
for i in dict:
    if (dict[i]>=1):
        print(i,end="    ")