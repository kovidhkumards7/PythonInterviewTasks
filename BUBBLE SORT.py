def bubbleSort(l):
    for i in range(len(l)-1):
        for j in range(len(l) - 1):
            if (l[j]>l[j+1]):
                l[j],l[j+1] = l[j+1],l[j]


size = int(input("enter size of the list  "))
list = [input("enter list element  ")for i in range(0,size)]
print("before sorting ",list)
bubbleSort(list)
print("after sorting ",list)
