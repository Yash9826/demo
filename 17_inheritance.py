class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def getData(self):
        print(f"{self.name},{self.age}{self.location}")
        
class Child(Parent):
    def __init__(self, name, age,location):
        Parent.__init__(self,name, age)
        self.location = location
        
    def getDataChild(self):
        print(f"{self.name},{self.age}{self.location}")
      

p1 = Child("yash",22,"bangluru")
p1.getData()    
p1.getDataChild()      

        