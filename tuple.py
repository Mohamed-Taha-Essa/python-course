#tuple is immutable
#list is mutable 
#when want date be safe not change
# memory efficient

# point = (10 ,20)
# colors = ('red' , 'greed','blue')
# one= (4,)
# empty = ()
# print(type(point))
# print(point)

# print(colors[0])
# colors[0] = 'yellow'


# a ,b =(10,20,30)
# print(a)
# print(b)

# a,*b ,c = [2,1,5,4,8,7]
# print(a)
# print(b)
# print(c)
a =[5,8,7,6,9]
b = [5,4,7,a]
print(a)
print(b)
print(b[-1])
#[5,4,7,5,8,7,6,9]
print(*a)
b = [*a,10,20]
print(b)