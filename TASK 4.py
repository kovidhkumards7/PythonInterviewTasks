a=float(input("enter age  "))
if (a>=0) and (a<=1):
    print("ur an infant ('-')")
elif(a>1) and (a<=18):
    print("ur a child ('-')")
elif(a>18) and (a<=60):
    print("ur an adult ('-')")
elif(a>60):
    print("ur a senior citizen ('-')")
elif (type(a)!=int):
    print('u hav an invalid age')