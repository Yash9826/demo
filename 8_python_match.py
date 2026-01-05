day = 7
match day:
    case 1:
        print("mon")
    case 2:
        print("tue")
    case 3:
        print("wed")
    case 4|5|6|7:
        print("generic")   
    case _:
        print("not found")  
        
        
i = 1
while i <= 6:
    i += 1
else:
    print("i was exhausted..")    
    

for i in range(1,6,2):
    print(i)    
    
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in reversed(adj):
    for f in reversed(fruits):
        print(a," ",f)    
        
        
for a in adj[::-1]:
    for f in fruits[::-1]:
        print(a," ",f)         
                   
        