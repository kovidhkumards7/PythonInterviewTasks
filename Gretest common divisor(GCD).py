# Greatest common divisor(GCD) of multiple numbers
print("To find GREATEST COMMON DIVISOR OF MULTIPLE NUMBERS")
size = int(input("enter the number of numbers to find out GCD  "))
listOfNumbers = [int(input("enter numbers  "))for i in range(size)]
listOfNumbers.sort()
print("Entered numbers are   ",listOfNumbers)
for i in range(listOfNumbers[0],1,-1):
    count = 0
    for j in listOfNumbers:
        if (j%i==0):
            count+=1
    if (count==len(listOfNumbers)):
        print("Thee GCD of all the entered numbers is  ",i)
        quit()
