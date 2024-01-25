
#Functions
'''
def addition(a,b):
    c = a + b
    print(c)

def substraction(a,b):
    c = a - b
    return c

def operation(a,b):
    add = a+b
    sub = a-b
    return add,sub

addition(20,30)
output = substraction(40,30)
print(output)

a,s = operation(20,30)
print(a)
print(s)

'''

#File Operations

#Write, Read

'''
fhandle = open('readme.txt','a')
fhandle.write('\nHow are you?')
fhandle.close()
'''
'''
fhandle = open('readme.txt')
data = fhandle.read()
print(data)
fhandle.close()
'''
'''
fhandle = open('readme.txt')
for line in fhandle:
    print(line)
fhandle.close()
'''
'''
fhandle = open('readme.txt')
data = fhandle.read()
value = input('Enter anything to search : ')
if value in data:
    print('Yes, Present')
else:
    print('Not Present')
fhandle.close()
'''
'''
fhandle = open('readme.txt')
counter = 0
for line in fhandle:
    counter = counter + 1
print(counter)
'''
#fhandle = open('readme.txt')

'''
for line in open('readme.txt'):
    print(line)
'''
'''
with open('readme.txt') as fhandle:
    for line in fhandle:
        print(line)
'''
#OOPS
#SQLite


#Data Structures in Python

#Program - Algorithms or Data structure
#1) List
#2) Dictionary
#3) Tuple
#4) Set




#Tuple

a,b,c = (1,2,3)
print(a)
print(b)
tuple1 = (4,2,2)
tuple2 = (2,5)
print(tuple1>tuple2)
mydict = {'Mahesh':1000,'Suresh':2000,'Ganesh':3000}
items = mydict.items()
print(items)










#Dictionary
'''
mydict = {'Mahesh':1000,'Suresh':2000,'Ganesh':3000}

value = mydict.get('Rahul','NA')
print(value)
'''
'''
mydict = {'Mahesh':1000,'Suresh':2000,'Ganesh':3000}
keys = mydict.keys()
print(keys)
values = mydict.values()
print(values)
'''







'''
fhandle = open('readme.txt')
data = fhandle.read()  #data = 'Mahesh is my name'
words = data.split()   #words = ['Mahesh','is','my','name']
mydict = dict()
for word in words:
    if word not in mydict:
        mydict[word] = 1
    else:
        mydict[word] = mydict[word] + 1
print(mydict)
fhandle.close()
'''







'''
print(employee)
employee['Rajesh'] = 5000
print(employee)
del employee['Rajesh']
print(employee)
'''

'''
if 'Rajesh' not in employee:
    print('Yes, Present')
else:
    print('Not Present')
'''


'''
print(employee['Mahesh'])
print(employee['Suresh'])
print(employee['Ganesh'])
for i in employee:
    print(i,employee[i])
'''





#List
'''
schoolfriends = ['Mahesh','Suresh','Ganesh','Ramesh']
collegefriends = ['Neha','Jaya','Sugandha','Dolly','Rekha','Megha']

allfriends = schoolfriends + collegefriends


mylist = list()

mylist.append('Mahesh')
mylist.append('Ganesh')
mylist.append('Suresh')
print(mylist)
mylist.remove('Suresh')
print(mylist)
mylist.insert(1,'Richa')
print(mylist)
mylist.pop(1)
print(mylist)
for i in range(0,2):
    print(mylist[i])

'''




'''
print(dir(list()))
print(len(allfriends))
'''


'''
print('Neha' not in allfriends)
if 'Neha' in allfriends:
    print('YEs')
else:
    print('Nope')
'''



'''
print(allfriends)
print(allfriends[1:3])
print(allfriends[1:])
print(allfriends[:5])
print(allfriends[:])
'''


'''
print(schoolfriends[0])
print(schoolfriends[1])
for i in schoolfriends:
    print(i)
schoolfriends[0] = 'Rajesh'
print(schoolfriends)
'''

















































