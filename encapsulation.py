# hide data
#public propereties
"""
class Person:
    def __init__(self , name , age) -> None:
        self.name = name
        self.age = age

p = Person('ahmed' ,32)
print(p.name, p.age)
p.name = 'ali'
p.age ='25'
print(p.name, p.age)
"""
#prtected concept
"""class Person:
    def __init__(self , name , age) -> None:
        self.name = name
        self._age = age  #protected

p = Person('ahmed' ,32)
print(p.name, p._age)
p.name = 'ali'
p._age ='25'
print(p.name, p._age)"""


# private properties
#
# class Person:
#     def __init__(self , name , age) -> None:
#         self.name = name
#         self.__age = age  #private

# p = Person('ahmed' ,32)
# print(p.name, p.__age)#AttributeError: 'Person' object has no attribute '__age'

# p.name = 'ali'
# p.__age ='25'
# print(p.name, p.__age)

#using getter and setter method
# class Person:
#     def __init__(self , name , age) -> None:
#         self.name = name
#         self.__age = age  #private
#     def get_age(self):
#         return self.__age
#     def set_age(self ,age):
#         if age>0:
#             self.__age =age
#         else:
#             print('age must be positive ')

# p = Person('ahmed' ,32)
# print(p.get_age())
# p.set_age(55)
# print(p.get_age())
# p.set_age(-5)
# property

# class Person:
#     def __init__(self , name , age) -> None:
#         self.name = name
#         self.__age = age  #private
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self ,age):
#         if age>0:
#             self.__age =age
#         else:
#             print('age must be positive ')

#     @age.deleter
#     def age(self):
#         print('deleting property')
#         del self.__age

# p = Person('ahmed' ,32)
# print(p.age)
# p.age = 66
# print(p.age)
# p.age = -5
# del p.age

# print(p.age)



# class Calculator:
#     def __init__(self) -> None:
#         self.result = 0


#     def __validate(self,num):
#         if not isinstance(num ,(int ,float)):
#             return False
#         return True

#     def add(self ,num):
#         if self.__validate(num):
#             self.result += num
#         else:
#             print('invalid number')
# calc = Calculator()
# calc.add(5)
# calc.add(6)
# calc.add(-6)
# calc.add(8)
# calc.add('ljl')
# print(calc.result)
# # calc.__validate(54)
# print(isinstance(calc ,Calculator))
#
#

# class Person:
#     def __init__(self , name , age) -> None:
#         self.name = name
#         self.__age = age  #private
#     def get_age(self):
#         return self.__age
#     def set_age(self ,age):
#         if age>0:
#             self.__age =age
#         else:
#             print('age must be positive ')

# p = Person('ali' , '66')
# print(p._Person__age)
# print(p.__age)

class Base:
    def __init__(self) -> None:
        self.__value = 'base'

    def shwo_base(self):
        return self.__value

class Child(Base):
    def __init__(self) -> None:
        super().__init()
        self.__value = 'child'

    def show_child(self):
        return self.__value
#_Base__value
#_Child__value
c = Child()
print(c.show_base())
print(c.show_child())
