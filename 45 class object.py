class car: 
    def __init__(self,name,cost,brand):
        self.name=name
        self.cost=cost
        self.brand=brand
    def move(self):
        return "car moves on road"
c=car("toyato",120000,"gochi")
print(c.name)            
print(c.move())