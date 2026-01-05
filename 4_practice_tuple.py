thistuple = ("apple",)
print(type(thistuple))
print(thistuple)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
green,*red,yellow = fruits
print(green,yellow,red)

for i in range(len(fruits)):
    print(fruits[i])
    
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i+1    




