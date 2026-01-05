def test():
    return "bad world"

# t = test()
# print(t)

print(test())


def show(fname,name = "world"):
    print("bad",name,fname)
    
show("khuddar",name="matlabi")
show("khuddar")


def demo(name,/):
    print("hello",name)
    
demo("jack")    

def demo2(*,name):
    print("hello",name)
    
demo2(name = "jack from keyord args") 

def myFun(a,b,/ ,*,c=33,d=44):
    print(a,b,c,d)
    
myFun(1,2)    
