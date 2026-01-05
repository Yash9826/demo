x = lambda a : a+10
print(x(5))


x = lambda a,b : a*b
print(x(2,3))


def myfunc(n):
    return lambda a : a*n

d = myfunc(2)
t = myfunc(3)
print(d(111))
print(t(111))

numbers = [1,2,3,4,5,6,7,8]
temp = list(map(lambda x : x*2,numbers))
print(temp)

numbers = [1,2,3,4,5,6,7,8]
temp = list(filter(lambda x: x%2 != 0,numbers))
print(temp)

numbers = ["apple", "pie", "banana", "cherry"]
temp = sorted(numbers,key=lambda x: len(x))
print(temp)

