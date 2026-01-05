# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
# p1 = Person("yash","36")
# print(p1.name)
# print(p1.age)


# class Person:
#     def __init__(self,name,age=22):
#         self.name = name
#         self.age = age
        
# p1 = Person("yash")
# p2 = Person("pandey",30)
# print(p1.name)        
# print(p1.age)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def getData(self):
#         print(f"name = {self.name} and age = {self.age}")
        
# p1 = Person("yash",22)
# p1.getData()  


# class Person:
#     def __init__(self,name):
#         self.name = name          
        
#     def greet(self):
#         return f"hello! {self.name}"
    
#     def namaste(self):
#         greet = self.greet()
#         return f"{greet}.How are you!!"
    
# p1 = Person("yash")
# msg = p1.namaste()
# print(msg)  
# print(p1.name)   

# p1.name = "anna"
# print(p1.name)
# msg = p1.namaste()
# print(msg)

# class Person:
#     universal = "human"
    
#     def __init__(self,name):
#         self.name = name 
    
#     def getData(self):
#         print("name = ",self.name)
        
# p1 = Person("yash")
# p2 = Person("honey")

# print(p1.name,p2.name)
# print(p1.universal,p2.universal)

# #to add more details to a specific object and not all
# p1.age = 22
# p2.location = "gunjur"

# print(p1.age)
# print(p2.location)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def getData(self):
        print(f"You are now {self.age} year old")
        self.age += 1
        
    def __str__(self):
        return(f"{self.name},{self.age}")    
        
p1 = Person("yash",22)
p1.getData()              
p1.getData()  
print(p1)            
             
        
 
             
               
               
               
        