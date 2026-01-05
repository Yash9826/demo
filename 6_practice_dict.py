thisdict = {
    "name" : "yash",
    "age" : 22,
    "location" : "banglore",
      "colors": ["red", "white", "blue"]
}
# print(thisdict)
# print(thisdict["name"])
# print(thisdict["colors"][0])

x = thisdict.get("colors")
y = thisdict.keys()
z = thisdict.values()
a = thisdict.items()

print(a)

thisdict['name'] = "yash chawda"
print(thisdict)

thisdict.update({"name" : "yash chawda kanasiya"})
print(thisdict)

