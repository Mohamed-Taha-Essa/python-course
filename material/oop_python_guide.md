# Introduction to Object-Oriented Programming (OOP) in Python

## 1. What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around **objects** rather than functions and logic alone. An object bundles together **data** (attributes) and **behavior** (methods) into a single unit.

The four main pillars of OOP are:

| Pillar | Meaning |
|---|---|
| **Encapsulation** | Bundling data and methods together, hiding internal details |
| **Abstraction** | Exposing only relevant details, hiding complexity |
| **Inheritance** | Creating new classes based on existing ones |
| **Polymorphism** | Objects of different classes responding to the same interface differently |

---

## 2. Class and Object — A Real Example

A **class** is a blueprint. An **object** (or instance) is a concrete thing built from that blueprint.

Think of `Car` as a blueprint — it describes what every car has (wheels, color, brand) and what every car can do (drive, brake). A specific car, like "my red Toyota," is an **object** created from that blueprint.

```python
class Car:
    # Class attribute (shared by all objects of this class)
    wheels = 4

    def __init__(self, brand, color, speed=0):
        # Instance attributes (unique to each object)
        self.brand = brand
        self.color = color
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.color} {self.brand} is now going {self.speed} km/h")

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        print(f"{self.color} {self.brand} slowed down to {self.speed} km/h")

    def __str__(self):
        return f"Car(brand={self.brand}, color={self.color}, speed={self.speed})"


# Creating objects (instances) from the Car class
car1 = Car("Toyota", "Red")
car2 = Car("Tesla", "Black")

car1.accelerate(40)   # Red Toyota is now going 40 km/h
car2.accelerate(80)   # Black Tesla is now going 80 km/h
car1.brake(10)        # Red Toyota slowed down to 30 km/h

print(car1)  # Car(brand=Toyota, color=Red, speed=30)
print(car2)  # Car(brand=Tesla, color=Black, speed=80)

print(car1.wheels)  # 4 (class attribute, shared)
print(car2.wheels)  # 4
```

**Key takeaway:** `Car` is the class (blueprint). `car1` and `car2` are objects (instances) — each has its own state (`brand`, `color`, `speed`) but shares the same behavior (`accelerate`, `brake`) defined in the class.

---

## 3. "Everything in Python is an Object"

This is one of Python's core design philosophies. Numbers, strings, functions, classes, modules — literally everything — are objects, meaning they all have a type, live in memory, and belong to a class.

```python
x = 10
print(type(x))          # <class 'int'>
print(isinstance(x, object))  # True

s = "hello"
print(type(s))          # <class 'str'>

def greet():
    pass
print(type(greet))      # <class 'function'>

class Dog:
    pass
print(type(Dog))        # <class 'type'>  -> even classes are objects (instances of 'type')

print(type(int))        # <class 'type'>
print(type(type))       # <class 'type'>  -> 'type' is the object that creates classes
```

Since everything is an object, everything has attributes and methods you can inspect:

```python
print((10).bit_length())     # 4  -> int has methods
print("hello".upper())       # HELLO -> str has methods
print(greet.__name__)        # greet -> functions have attributes too
```

---

## 4. Is Python Fully OOP or Partially OOP?

**Python is a multi-paradigm language, and it is considered PARTIALLY object-oriented (a hybrid language).**

### Arguments that Python IS object-oriented:
- Everything is an object (as shown above), even primitive types and functions.
- It supports all four pillars: encapsulation, abstraction, inheritance, polymorphism.
- Classes, objects, and instance methods are first-class citizens.

### Arguments that Python is NOT *purely* / *fully* OOP:
- You can write entire programs using only functions, without ever defining a class (procedural style) — Python does not force you to use classes, unlike Java where every piece of code must live inside a class.
- Python supports multiple paradigms simultaneously: **procedural** (plain functions/scripts), **functional** (`map`, `filter`, `lambda`, `reduce`), and **object-oriented**.
- Python allows global functions (`print()`, `len()`, `sum()`) that exist outside of any class — in a "pure" OOP language like Java, every function must belong to a class.
- Python does not enforce strict encapsulation. There is no true `private`/`protected` access control — it's convention-based (`_protected`, `__private` name-mangling), and can still be accessed if you really want to.

```python
# Purely procedural, no classes needed — valid, idiomatic Python
def add(a, b):
    return a + b

print(add(3, 4))  # 7
```

**Conclusion:** Python is a **multi-paradigm language that is deeply OOP under the hood** (everything is an object) **but does not force the OOP style on the developer** — making it *partially* / *pragmatically* object-oriented rather than a "pure" OOP language like Java or Smalltalk.

---

## 5. Inheritance in Python

**Inheritance** allows a class (child/subclass) to reuse and extend the attributes and methods of another class (parent/superclass). It promotes code reuse and models "is-a" relationships (a `Dog` **is an** `Animal`).

### Basic Syntax

```python
class Parent:
    def method(self):
        pass

class Child(Parent):  # Child inherits from Parent
    pass
```

### Types of Inheritance in Python

Python supports **5 types** of inheritance:

1. **Single Inheritance** — one child inherits from one parent.
2. **Multiple Inheritance** — one child inherits from more than one parent.
3. **Multilevel Inheritance** — a chain: grandparent → parent → child.
4. **Hierarchical Inheritance** — multiple children inherit from the same parent.
5. **Hybrid Inheritance** — a combination of two or more types above.

---

### 5.1 Single Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Rex")
d.eat()   # Rex is eating   (inherited from Animal)
d.bark()  # Rex says Woof!  (defined in Dog)
```

### 5.2 Multiple Inheritance

```python
class Flyer:
    def fly(self):
        print(f"{self.name} is flying")

class Swimmer:
    def swim(self):
        print(f"{self.name} is swimming")

class Duck(Flyer, Swimmer):  # inherits from BOTH Flyer and Swimmer
    def __init__(self, name):
        self.name = name

d = Duck("Donald")
d.fly()   # Donald is flying
d.swim()  # Donald is swimming
```

### 5.3 Multilevel Inheritance

```python
class Animal:
    def eat(self):
        print("Animal eats")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):        # Dog -> Mammal -> Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()   # inherited from Animal
d.walk()  # inherited from Mammal
d.bark()  # defined in Dog
```

### 5.4 Hierarchical Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

# Both Cat and Dog inherit from the same parent: Animal
c = Cat("Whiskers")
d = Dog("Rex")
c.eat(); c.meow()
d.eat(); d.bark()
```

### 5.5 Hybrid Inheritance

```python
class Animal:
    def eat(self):
        print("Animal eats")

class Pet:
    def play(self):
        print("Pet plays")

class Dog(Animal):        # multilevel branch
    def bark(self):
        print("Dog barks")

class ServiceDog(Dog, Pet):  # multiple + multilevel combined = hybrid
    def assist(self):
        print("ServiceDog assists")

s = ServiceDog()
s.eat(); s.bark(); s.play(); s.assist()
```

### `super()` and Method Overriding

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call the parent's __init__
        self.breed = breed

    def speak(self):              # method overriding
        super().speak()           # still call parent's version if needed
        print(f"{self.name} says Meow (breed: {self.breed})")

c = Cat("Luna", "Persian")
c.speak()
# Luna makes a sound
# Luna says Meow (breed: Persian)
```

### Method Resolution Order (MRO)

With multiple inheritance, Python uses the **C3 linearization algorithm** to decide which method to call:

```python
class A:
    def hello(self): print("A")

class B(A):
    def hello(self): print("B")

class C(A):
    def hello(self): print("C")

class D(B, C):
    pass

D().hello()          # B  (follows MRO)
print(D.__mro__)     # (D, B, C, A, object)
```

---

## 6. Practice Tasks (10 Tasks on Inheritance & OOP)

Try to solve these yourself before checking any solution.

1. **Basic Class** — Create a `Person` class with attributes `name` and `age`, and a method `introduce()` that prints `"Hi, I'm <name> and I'm <age> years old."` Create two `Person` objects and call `introduce()` on each.

2. **Single Inheritance** — Create a class `Employee` that inherits from `Person` (from task 1) and adds a `salary` attribute and a method `show_salary()`. Override `introduce()` to also mention the job title.

3. **Multilevel Inheritance** — Create `Vehicle` → `Car` → `SportsCar`. `Vehicle` has `speed`, `Car` adds `brand`, `SportsCar` adds `top_speed` and a method `boost()` that increases `speed` toward `top_speed`.

4. **Multiple Inheritance** — Create `Camera` (method `take_photo()`) and `Phone` (method `make_call()`), then create `SmartPhone` that inherits from both. Instantiate it and call both methods.

5. **Hierarchical Inheritance** — Create a parent class `Shape` with a method `area()` that returns `0`. Create `Circle` and `Rectangle` subclasses that each override `area()` with the correct formula. Store several shape objects in a list and print each one's area using a loop (this also demonstrates polymorphism).

6. **Using `super()`** — Create a class `Book` with `title` and `price`. Create `EBook(Book)` that adds `file_size_mb` and uses `super().__init__()` to avoid repeating code. Add a `__str__` method for nice printing.

7. **Method Overriding & Polymorphism** — Create a base class `Animal` with a method `sound()` that returns `"..."`. Create `Dog`, `Cat`, and `Cow` subclasses that override `sound()`. Write a function `make_all_sounds(animals)` that takes a list of `Animal` objects and calls `sound()` on each, regardless of the exact subclass.

8. **Abstract-like Base Class** — Using the `abc` module, create an abstract class `PaymentMethod` with an abstract method `pay(amount)`. Create `CreditCard` and `PayPal` subclasses that implement `pay()` differently. (Research: `from abc import ABC, abstractmethod`.)

9. **Encapsulation + Inheritance** — Create a class `BankAccount` with a "private" attribute `__balance` (name-mangled), and methods `deposit()`, `withdraw()`, and `get_balance()`. Create `SavingsAccount(BankAccount)` that adds an `interest_rate` and a method `apply_interest()`.

10. **Check MRO and Type Everything** — Build a small hybrid-inheritance hierarchy of your own (at least 3 classes, using both single and multiple inheritance). Then, for one final object: (a) print its `type()`, (b) print `isinstance()` checks against every ancestor class, (c) print `ClassName.__mro__` to see the resolution order, and (d) explain in a comment why Python is considered "partially OOP" using at least one example from your own code.

---

### Bonus Tip
To check inheritance relationships programmatically, use:
```python
issubclass(Dog, Animal)      # True/False
isinstance(my_dog, Animal)   # True/False
Dog.__bases__                # (Animal,)
Dog.__mro__                  # Full resolution chain
```

Good luck, and remember: the best way to learn OOP is to build small projects (a `Library` system, a `Zoo` simulator, or a `Shape` calculator) using these exact patterns.
