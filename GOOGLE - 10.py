# GOOGLE CODE - 10 forGiven the value of n, we need to find the sum of the series where i-th term is sum of first i natural numbers.
# INote:- Sum of the series 1 + (1+2) + (1+2+3) + (1+2+3+4) + .. + (1+2+3+4+...+n) ......
# Input : 5
# Output : 35
num = int(input("enter a number  "))
list = []
count = 0
s = 0
while (count<num):
    count+=1
    list.append(count)
    s = s + sum(list)
print(s)
