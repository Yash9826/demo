fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
blank = []

for f in fruits:
    if "a" in f:
        blank.append(f)
        
data = [b.upper() for b in blank]   
print(data)  

data = [f if f != 'banana' else 'orange' for f in fruits ]  
print(data) 

fruits.sort(reverse=True)
print(fruits)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

thislist.reverse()
print(thislist)

# list_copy = thislist.copy()
# list_copy = list(thislist)
list_copy = thislist[:]
print(list_copy)







