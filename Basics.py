'''
dollars = input('Enter amount in dollars : ')
rupees = int(dollars) * 75
print("Amount in rupeess is "+str(rupees))
'''
#If Condition
'''
age = int(input('Enter your age : '))
gender = input('Select your gender m/f : ')

if gender == 'f':
    if age >=18:
        print('You are eligible')
    else:
        print('You are not eligible')
elif gender == 'm':
    if age >= 21:
        print('You are eligible')
    else:
        print('You are not eligible')
else:
    print('Invalid input')

'''

'''
if (age>=18 and gender=='f') or (age>=21 and gender=='m'):
    print('You are eligible ')
else:
    print('You are not eligible ')
'''
'''
#for loop
for i in range(10,0,-1):
    print(i)
'''
'''
n = 10
while n < 20:
    print('Hello Dear')
    n = n+1
'''
'''
for i in range(1,200):
    if i == 17:
        continue
    if i == 40:
        break
    print(i)
'''
'''
for i in [20,30,40,50,60,70,80]:
    print(i,end=" ")
'''
#Strings
'''
name = "Mahesh Rakheja"
print(name)
print(name[0])
print(name[1])
for i in name:
    print(i)
print(len(name))
'''
sentence = 'i hate you like i love you i hate you loke i love you'
words = sentence.split('like')
print(words)


#functions
#file operations
#data structures(list,dictionary,tuples)




'''
name = "  Mahesh  Rakheja  "
print(name.lstrip())
print(name.rstrip())
print(name.strip())
'''
'''
upsentence = sentence.upper()
print(sentence)
print(upsentence)
tisentence = sentence.title()
print(tisentence)
print(sentence.isupper())
print(upsentence.isupper())
'''




'''
print(sentence[0:10])
print(sentence[:10])
print(sentence[10:])
print(sentence[:])
print('z' not in sentence)
print(dir(''))
'''



