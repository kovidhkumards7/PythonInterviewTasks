size = int(input("enter size of the list  "))
list = [input("enter list element  ")for i in range(0,size)]
search = input("enter the search element  ")
def linearSearch(a,t):
    b = 0
    c = 0
    for i in a:
        if (t==i):
            b = 1
            break
        else:
            b = 0
            c+=1
    if (b==1):
        print("element ",t," found in position ",c+1)
    else:
        print("element not found")
linearSearch(list,search)
