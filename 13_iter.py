# myNumber = [1,2,3,4,5]
# num = iter(myNumber)

# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))


class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 11:
            x = self.a
            self.a  += 1
            return x 
        else:
            raise StopIteration
   
mynumber = MyNumber()
num = iter(mynumber)

# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))  
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))  
# print(next(num))  

for i in num:
    print(i)
    
    
import platform

x = dir(platform)
print(x)    