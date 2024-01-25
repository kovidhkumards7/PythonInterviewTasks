def binarySearch(list,search):
    low = 0
    high = len(list)-1
    b = 0
    while (low<=high) and (b==0):
        mid = (low + high) // 2
        if (search==list[mid]):
            b=1
            break
        elif (search>list[mid]):
            low=mid+1
        elif (search < list[mid]):
            high=mid-1
        else:
            b=0
    if (b==1):
        print("the search element ",search," is found at position ",mid+1)
    else:
        print("element ",search," not found")


size = int(input("enter size of the list  "))
list = [input("enter list element  ")for i in range(0,size)]
search = input("enter the search element  ")
list.sort()
binarySearch(list,search)