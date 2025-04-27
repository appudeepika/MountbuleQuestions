# SINGLE INHERITANCE
class animal:
    def make_sound(self):
        return "animals makes sound"
class dog(animal):
    def make_sound(self):
        return "bark"
a=animal()
d=dog()
print(a.make_sound())
print(d.make_sound())

# MULTIPLE INHERITANCE
class Animal:
    def speak(self):
        return "Some generic animal sound"
class Mammal:
    def breathe(self):
        return "Breathing air"
class Dog(Animal, Mammal):  
    def speak(self):
        return "Woof!"
dog = Dog()
print(dog.speak())  
print(dog.breathe())  

# MULTILEVEL INHERITANCE
class Animal:
    def speak(self):
        return "Some generic animal sound"
class Mammal(Animal):
    def breathe(self):
        return "Breathing air"
class Dog(Mammal):  
    def speak(self):
        return "Woof!"
dog = Dog()
print(dog.speak())  
print(dog.breathe())  

# hirearhical inheritance
class Animal:
    def speak(self):
        return "Some generic animal sound"
class dog(Animal):
    def speak(self):
        return "woof"
class cat(Animal):
    def speak(self):
        return "meow"
d=dog()
c=cat()
print(d.speak())  
print(c.speak())      
