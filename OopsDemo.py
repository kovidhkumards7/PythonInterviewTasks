class Car:

    def __init__(self,name,cost,color):
        self.name = name
        self.cost = cost
        self.color = color

    def increase_cost(self,cost):
        self.cost = self.cost + cost

    def get_cost(self):
        return self.cost
#broadcast.maheshrakheja.com

#11:00 am
#Sqlite Database
#SQL

class SubCar(Car):

    def change_color(self,color):
        self.color = color

#SQLite

sc = SubCar('Tata',5000,'Red')
print(sc.get_cost())
print(sc.color)
sc.change_color('Black')
print(sc.color)
sc.cost = sc.cost + 3000
print(sc.cost)