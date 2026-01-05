import json

data = '{"name":"yash", "age":"23","city":"banglore"}'
print(data)
x = json.loads(data)
print(x["age"])

data2 = {
    
    "name" : "yash",
    "age" : 30,
    "city" : "indore"
}
print(data)
y = json.dumps(data2)
print(y)
