# Problem - 18 : Problem to HANOI TOWER
n = int(input("enter the number of discs  "))
s = "source"
t = "tempravory"
d = "destination"
def hanoi(n,s,t,d):
    if (n==1):
        print("move disc ",n," from ",s," to ",d)
    else:
        hanoi(n-1,s,d,t)
        print("move disc ",n," from ",s," to ",d)
        hanoi(n-1,t,s,d)
a = hanoi(n,s,t,d)
print(a)