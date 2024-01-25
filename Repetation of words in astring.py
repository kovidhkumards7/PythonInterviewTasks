a=open("repeted words","w")
a.write("the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car")
a.close()
f=open("repeted words","r")
a=[]
b={}
for i in f:
    i.strip()
    a=i.split()
    for j in a:
        b[j]=b.get(j,0)+1
    print(b)



userEnteredString = input( "enter string  " )
stringInList = userEnteredString.split()
print( stringInList )
stringInDictionary = {}
for instant in stringInList:
    stringInDictionary[instant] = stringInDictionary.get(instant, 0) + 1
for instant in stringInDictionary:
    print( instant , stringInDictionary [instant] )
