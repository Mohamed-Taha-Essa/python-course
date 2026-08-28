import json

# x = '{"name" : "ahmed" , "age":25 , "city" : "ismailia"}'
# print(x)
# print(type(x))

# y = json.loads(x)
# print(type(y))
# print(y)
x = {"name":"ahmed" , "age":25 , "city":"ismailia"}
y = json.dumps(x)
print(y)
print(type(y))
# y = json.loads(y)
print(y[0])
print(y[1])
print(y[2])
for i in y :
    print(i)