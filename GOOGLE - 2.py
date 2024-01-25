# # GOOGLE CODE - 2 to print the first non repeating char in a user entered sentence
# u tube link  =  https://youtu.be/5co5Gvp_-S0


# # GOOGLE CODE to print the first non repeating char in a user entered sentence
a=input("enter a word  ")
b=[]
for i in range(0,len(a)):
    s=0
    for j in range(0,len(a)):
        if(a[i]==a[j]):
            s=s+1
    if(s==1):
        b.append(a[i])
print("The 1st non repeating letter in the entered sentence is  ",b[0])