import SqliteDemo

mydb = SqliteDemo.MyDatabase('studentinfo.db')
mydb.create_table()
while True:
    print('1)Insert Data')
    print('2)Delete Data')
    print('3)Update Data')
    print('4)Select Data')
    print('5) Exit')
    x = int(input('Select your choice : '))
    if x == 1:
        name = input('Enter name : ')
        number = input('Enter number :')
        mydb.insert_data(name,number)
    elif x == 2:
        id = input('Enter id : ')
        mydb.delete_data(id)
    elif x == 3:
        pass
    elif x == 4:
        mydb.select_data()
    elif x == 5:
        break
    else:
        print('Inavlid input.')

#Web Scrapping.
#http://broadcast.maheshrakheja.com