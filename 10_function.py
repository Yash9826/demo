def myFun(greet,*name):
    for i in name:
        print(greet,i)
        
        
myFun("hello","A","B","C") 


def sum(*numbers):
    s = 0
    s = [i+s for i in numbers] 
    print("sum = ",s)
    
sum(1,2,3,4,5)    
sum(10,20,30,40,50)    
sum(100,200,300,400,500)  


def modified(func):
    def inner(x):
        print(f"printing the data of {func.__name__}{x}")
        func(x)
        print(f"completed {func.__name__}{x}")
    return inner



@modified    
def test1(temp):
    print(f"{temp}function..")

@modified       
def test2(temp):
    print(f"{temp}function..")



test1("test1")
test2("test2")    
          
  