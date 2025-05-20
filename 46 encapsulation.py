class student:
    def __init__(self,name,age):
        self.name=name
        self._age=age
    def get_age(self):
        return self._age
    def set_age(self,new_age):
        if new_age>0:
            self._age=new_age
        else:
            print("age must br positive")
s=student("deepika",23)
print(s.get_age())
s.set_age(25)
print(s.get_age())
