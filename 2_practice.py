x = "yash"

def test():
    global x 
    x = "universal"
    print("Inside the function = ",x)

test()

print("outside the function = ",x)

temp = "Hello world"
print(temp[2:5]) #ll0

print(temp[:5])
print(temp[2:])
print(temp[-5:-2])

temp = "yCsh CHAWDA"
print(temp.upper())
print(temp.lower())
print(temp.strip())
print(temp.replace('C','a',-1))
print(temp.split("A"))

#formatting
price = 144.55
print(f"the price of this bag is {price:2F}")

print(temp.capitalize())
print(temp.casefold())


txt = "I love apples, apple are my favorite fruit."
x = txt.count("a")
x = txt.endswith(("fruit","."))
x = txt.encode()
print(x)

ls = ["yash","ram","pandey"]
ls_data = " ".join(ls)
print(ls_data)

# find = ls[0]
# if find == "yash":
#     print("Found the name in list")

# if(find := ls[0]) == 'yash':
#     print("Found the name in list with warlur operator")
    
# print(ls[0])
# if "ramm" in ls:
#     print("name found")   
    
ls[0:2] = ["ram","shyam"]
print(ls)

ls.insert(3,"honey")
print(ls)

ls.remove("pandey")
print(ls)
ls.pop(0)
print(ls)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
    
[print(x)for x in thislist if x.startswith('a')]    

