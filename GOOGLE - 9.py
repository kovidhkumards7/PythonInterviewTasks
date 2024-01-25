# GOOGLE CODE - 9 for sorting a particular sub array
size = int(input("enter size  "))
list = [int(input("enter number  "))for i in range(0,size)]
list1 = []
a = int(input("enter lower limit to start sorting  ")) - 1
b = int(input("enter upper limit to stop sorting  ")) - 1
print("the entered list is:",list)
for i in range(a,b+1):
    list1.append(list[i])
# print(list1)
list1.sort()
# print(list1)
newList = []
for i in range(0,a):
    newList.append(list [i])
for i in range(0,len(list1)):
    newList.append(list1 [i])
for i in range(b+1,len(list)):
    newList.append(list [i])
print("the sorted list is:",newList)