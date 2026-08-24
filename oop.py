
# student_name = "Ali"
# student_age = 20
# student_address = 'ismailia'
# student_phone = '4632121'

# def display_student(name, age):
#     print(f"Name: {name}")
#     print(f"Age: {age}")

# display_student(student_name, student_age)
#

#inheritance
#encapsulation
#polymorphism
#abstract

#design for mobile: red , green , blue
# screen =  min ,small , medium , large
#weight = light , medium , heavy

# 100000 product

from zlib import DEF_BUF_SIZE


class calculator:
    def sum(self ,x , y ):
        return x +y

    def mul(self ,x ,y):
        return x*y

c = calculator()
c1 = calculator()
# print(c.sum(2,3))
# print(c1.mul(2,3))

# name = 'ali'

# print('ali'.upper() , 'ali'.lower())

# numbers = [ 2,5,48,9,6]
# numbers.append(77)
# print(type(numbers))
# class Calculator:
#     def __init__ (self ,x :int ,y:int):
#         self.x =x
#         self.y =y

#     def sum(self):
#         return  self.x+self.y

#     def mul(self):
#         return self.x*self.y

# c = calculator(44 ,55)
# c1 = calculator(77,88)

# print(c.sum())
# print(c1.mul())
#

#---multi level inheritence
#

# class Animal:
#     def eat(self):
#         print('eating')

# class Mammal(Animal):
#     def walk(self):
#         print('walking')


# class Dog(Mammal):
#     def bark(self):
#         print('barking')


# d = Dog()
# d.eat()
# d.walk()
# d.bark()


### hierarhical inhertance

# class Animal:
#     def eat(self):
#         print('eating')


# class Dog(Animal):
#     def bark(self):
#         print('barking')
# class Cat(Animal):
#     def meow(self):
#         print('meow')

# d = Dog()
# d.eat()

# c= Cat()
# c.eat()
# c.meow()


# multiple inheritance
#
class Father:
    def work(self):
        print('father')

class Mother:
    def cook(self):
        print('cook')
    def work(self):
        print('work from Mother')

class Child(Mother,Father):
  pass

c = Child()
c.work()
c.cook()
print(Child.mro())
