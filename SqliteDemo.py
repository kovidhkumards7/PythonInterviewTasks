import sqlite3

class MyDatabase:

    def __init__(self,dbname):
        self.db = sqlite3.connect(dbname)
        if self.db != None:
            print('Database created.')

    def create_table(self):
        query = "create table if not exists stud (id integer primary key autoincrement,name text not null,number(10) text not null);"
        self.db.execute(query)
        print('Table created successfully.')

    def insert_data(self,name,number):
        query = "insert into stud (name,number) values ('{}','{}');".format(name,number)
        self.db.execute(query)
        self.db.commit()

    def delete_data(self,id):
        query = "delete from stud where id={};".format(id)
        self.db.execute(query)
        self.db.commit()

    def select_data(self):
        query = "select * from stud;"
        rows = self.db.execute(query)
        for row in rows:
            print(row)


