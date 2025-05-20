class animal():
    def make_sound(self):
        print("animals are good")
class dog(animal):
    def make_sound(self):
        print("bark") 
class cat(animal):
    def make_sound(self):
        print("meow-meow")  
a=animal()            
d=dog()
c=cat()
d.make_sound()
c.make_sound()
a.make_sound()


# METHOD OVERLOADING
class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
c=calculator()
print(c.add(3))   
print(c.add(3,3)) 
print(c.add(3,4,5))  

# *args
class calculator:
    def add(self,*args):
        return args
c=calculator()
print(c.add(3))   
print(c.add(3,3)) 
print(c.add(3,4,5))  
