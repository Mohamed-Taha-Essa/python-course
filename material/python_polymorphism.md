# Python Polymorphism — A Beginner's Guide

## Table of Contents
1. [What is Polymorphism?](#what-is-polymorphism)
2. [Function Polymorphism](#function-polymorphism)
3. [Class Polymorphism](#class-polymorphism)
4. [Inheritance Class Polymorphism](#inheritance-class-polymorphism)
5. [Polymorphism with Operators](#polymorphism-with-operators)
6. [Duck Typing: Polymorphism Without Inheritance](#duck-typing-polymorphism-without-inheritance)
7. [Abstract Classes: Enforcing Polymorphism](#abstract-classes-enforcing-polymorphism)
8. [Method Overloading vs Method Overriding](#method-overloading-vs-method-overriding)
9. [Why Polymorphism Matters](#why-polymorphism-matters)
10. [Key Takeaways](#key-takeaways)

---

## What is Polymorphism?

The word **"polymorphism"** means **"many forms"**. In programming, it refers to methods, functions, or operators that share the **same name** but can be executed on **many different objects or classes**, each producing its own appropriate result.

In simple terms: the same piece of code (a function call, a method name, an operator) behaves differently depending on *what* it's used with.

```python
len("Hello")          # works on a string
len(["a", "b", "c"])  # works on a list
len({"a": 1, "b": 2}) # works on a dictionary
```

You call `len()` the exact same way every time, but Python figures out the right behavior based on the type of object you gave it. That's polymorphism in action.

---

## Function Polymorphism

An example of a Python function that can be used on different types of objects is the built-in `len()` function. It behaves differently depending on the data type it receives.

### String

For strings, `len()` returns the number of characters:

```python
x = "Hello World!"

print(len(x))   # 12
```

### Tuple

For tuples, `len()` returns the number of items in the tuple:

```python
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))   # 3
```

### Dictionary

For dictionaries, `len()` returns the number of key/value pairs in the dictionary:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))   # 3
```

### List and Set (extra examples)

The same idea extends to other built-in types too:

```python
mylist = [1, 2, 3, 4]
print(len(mylist))    # 4

myset = {1, 2, 3}
print(len(myset))     # 3
```

In every case, `len()` is a **single function** — but internally, Python calls a different piece of logic depending on the object's type (`str`, `tuple`, `dict`, `list`, `set`), because each of these types defines its own `__len__()` method behind the scenes. That's why `len()` is a perfect beginner example of polymorphism.

---

## Class Polymorphism

Polymorphism is often used with **class methods**, where multiple classes can have a method with the **same name**, but each class implements it differently.

For example, say we have three classes — `Car`, `Boat`, and `Plane` — and they all have a method called `move()`:

```python
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")        # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")      # Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

# Output:
# Drive!
# Sail!
# Fly!
```

Look at the `for` loop at the end. Because of polymorphism, we can call `x.move()` on all three objects using the exact same code, even though `Car`, `Boat`, and `Plane` are completely unrelated classes (none of them inherit from each other). Python doesn't check what type `x` is — it just looks for a `move()` method on whatever object it's given, and runs it.

---

## Inheritance Class Polymorphism

What about classes that share a **parent class**? Can polymorphism be used there too?

**Yes.** If we take the example above and create a parent class called `Vehicle`, then make `Car`, `Boat`, and `Plane` **child classes** of `Vehicle`, the child classes automatically inherit `Vehicle`'s methods — but they can also **override** them with their own version.

```python
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")        # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")      # Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
```

**What's happening here:**
- Child classes automatically inherit the properties (`brand`, `model`) and methods (`move()`) from the parent class `Vehicle`.
- The `Car` class body is just `pass` — it's empty — but it still has `brand`, `model`, and `move()`, all inherited directly from `Vehicle`. Calling `car1.move()` prints `"Move!"`, the parent's default behavior.
- `Boat` and `Plane` also inherit from `Vehicle`, but they each **override** the `move()` method with their own version, so `boat1.move()` prints `"Sail!"` and `plane1.move()` prints `"Fly!"` instead of the parent's `"Move!"`.

This is called **method overriding**, and it's one of the most common ways polymorphism shows up in real object-oriented code. Because of polymorphism, we can execute the same method call (`x.move()`) across every object in the loop, and each one automatically runs its own correct version — Python decides which version to run **at runtime**, based on the actual object's class.

---

## Polymorphism with Operators

Polymorphism isn't limited to functions and methods — Python's built-in **operators** are polymorphic too. The same operator behaves differently depending on the data types involved:

```python
print(3 + 5)          # 8            -> adds two numbers
print("a" + "b")      # "ab"         -> joins two strings
print([1, 2] + [3, 4]) # [1, 2, 3, 4] -> merges two lists
```

The `+` symbol is one single operator, but it means "add," "concatenate," or "merge" depending on what it's applied to. This works because each type (`int`, `str`, `list`) defines its own version of the special method `__add__()`, which is what actually runs when you use `+`. You can even define `__add__()` on your own custom classes to make `+` work with them too — this is called **operator overloading**, a specific form of polymorphism.

---

## Duck Typing: Polymorphism Without Inheritance

Notice that in the **Class Polymorphism** example above, `Car`, `Boat`, and `Plane` weren't related by inheritance at all — they were just three separate classes that happened to each have a `move()` method. Python still let us call `x.move()` on all of them without complaint.

This works because Python uses **duck typing**: *"If it walks like a duck and quacks like a duck, it's treated like a duck."* Python doesn't check what class an object belongs to before calling a method — it just checks whether the object has that method, and calls it. If it does, great; if not, you get an error at that point.

```python
class Duck:
    def sound(self):
        return "Quack!"

class Dog:
    def sound(self):
        return "Woof!"

def make_sound(animal):
    print(animal.sound())   # no type-checking here at all

make_sound(Duck())   # Quack!
make_sound(Dog())    # Woof!
```

This is a more relaxed, flexible form of polymorphism than what you might see in strictly typed languages, and it's very common in everyday Python code.

---

## Abstract Classes: Enforcing Polymorphism

Sometimes you want to **guarantee** that every subclass implements a certain method, instead of just hoping they remember to. Python's `abc` module (Abstract Base Classes) lets you enforce this:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass   # no implementation here — subclasses MUST provide one

class Car(Vehicle):
    def move(self):
        print("Drive!")

# vehicle = Vehicle()   # TypeError: Can't instantiate an abstract class
car1 = Car()
car1.move()             # Drive!
```

If a subclass forgets to implement `move()`, Python raises a `TypeError` the moment you try to create an instance of it. This is a stricter, safer way to design polymorphic class hierarchies for larger projects, while the plain inheritance example above is perfectly fine for smaller or beginner-level programs.

---

## Method Overloading vs Method Overriding

These two terms sound similar and are both forms of polymorphism, but they work very differently — and it's important to know that **Python only supports one of them natively**.

### Method Overloading (Not natively supported in Python)

**Overloading** means having **multiple methods with the same name in the same class**, but with different numbers or types of parameters. The correct version is chosen automatically based on how many/what type of arguments you pass in.

This is common in languages like Java or C++:

```java
// Java example — NOT Python
class Calculator {
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
    int add(int a, int b, int c) { return a + b + c; }
}
```

Java allows three separate `add()` methods to exist side by side, and picks the right one based on the arguments given.

**Python does not support this.** If you define a method more than once in a class, Python doesn't keep multiple versions — it simply **overwrites** the earlier one. Only the last definition survives:

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):   # this OVERWRITES the method above
        return a + b + c

calc = Calculator()
print(calc.add(2, 3, 4))   # 9 — works
print(calc.add(2, 3))      # TypeError: add() missing 1 required positional argument: 'c'
```

The first `add(self, a, b)` no longer exists at all — Python replaced it. There's no "choosing the right version based on arguments" happening here, unlike in Java.

### How Python Fakes Overloading

Since true overloading isn't available, Python developers simulate the same *effect* using other tools:

**1. Default arguments**

```python
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))       # 5  — c defaults to 0
print(calc.add(2, 3, 4))    # 9
```

**2. `*args` (variable number of arguments)**

```python
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(2, 3))          # 5
print(calc.add(2, 3, 4, 5))    # 14
```

**3. `functools.singledispatch` (dispatch based on argument type)**

```python
from functools import singledispatchmethod

class Printer:
    @singledispatchmethod
    def show(self, value):
        print(f"Value: {value}")

    @show.register
    def _(self, value: int):
        print(f"Integer: {value}")

    @show.register
    def _(self, value: str):
        print(f"String: {value}")

p = Printer()
p.show(5)        # Integer: 5
p.show("hi")     # String: hi
p.show(3.14)     # Value: 3.14  (falls back to the default)
```

These aren't "real" overloading under the hood — they're single methods written flexibly enough to handle different inputs. But from the outside, they achieve a similar result to what overloading gives you in other languages.

### Method Overriding (Fully supported in Python)

**Overriding**, unlike overloading, **is** natively and fully supported in Python. It means a **child (subclass)** provides its **own implementation** of a method that's already defined in its **parent class**, replacing the parent's version whenever it's called on a child object.

This is exactly what happened earlier in the [Inheritance Class Polymorphism](#inheritance-class-polymorphism) section with `Vehicle`, `Boat`, and `Plane`. Let's break down precisely how and why it works:

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Boat(Vehicle):
    def move(self):          # <-- overrides Vehicle.move()
        print("Sail!")

boat1 = Boat("Ibiza", "Touring 20")
boat1.move()   # Sail!  — NOT "Move!"
```

**How Python decides which `move()` to run:**

1. `Boat` inherits from `Vehicle`, so it starts out with access to everything `Vehicle` defines, including `move()`.
2. But `Boat` **also defines its own `move()` method** with the exact same name.
3. When you call `boat1.move()`, Python looks for `move()` starting on the **object's own class first** (`Boat`), not the parent. It finds `Boat.move()` right away and stops looking — so it never even reaches `Vehicle.move()`.
4. This lookup order is called the **Method Resolution Order (MRO)**: Python always checks the actual class of the object before checking any parent classes, walking up the inheritance chain from most specific to least specific.

You can prove this lookup order yourself:

```python
print(Boat.__mro__)
# (<class '__main__.Boat'>, <class '__main__.Vehicle'>, <class 'object'>)
```

Python checks `Boat` first, then `Vehicle`, then the base `object` class — stopping at the first match it finds.

**Calling the parent's version anyway with `super()`**

Sometimes you don't want to fully replace the parent's method — you want to **extend** it, running the parent's code *and then* adding your own. The `super()` function lets you do this:

```python
class Vehicle:
    def move(self):
        print("Move!")

class Plane(Vehicle):
    def move(self):
        super().move()        # runs Vehicle's original move() first
        print("Fly!")         # then adds Plane's own behavior

plane1 = Plane()
plane1.move()
# Output:
# Move!
# Fly!
```

This is useful when the child's behavior should build on top of the parent's behavior, rather than throw it away completely.

### Overloading vs Overriding — Side by Side

| | **Overloading** | **Overriding** |
|---|---|---|
| Definition | Multiple methods, same name, different parameters | Subclass redefines a method already in its parent class |
| Supported natively in Python? | ❌ No | ✅ Yes |
| Where it happens | Within the same class | Between a parent class and a child class |
| How Python handles it | Later definitions silently overwrite earlier ones | Uses Method Resolution Order (MRO) to pick the most specific version |
| Python workaround | Default args, `*args`/`**kwargs`, `functools.singledispatch` | No workaround needed — works out of the box |
| Common use case | Accepting flexible/varied input to one method | Customizing inherited behavior for a specific subclass |

---

## Why Polymorphism Matters

| Benefit | Explanation |
|---|---|
| **Less repetitive code** | Write one loop or one function that works for many types, instead of separate code for each one |
| **Easier to extend** | Add a brand-new class (like `Motorcycle`) with its own `move()` method, and existing code (like the `for x in (...): x.move()` loop) works with it immediately — no changes needed |
| **Cleaner logic** | Avoids long chains of `if isinstance(x, Car): ... elif isinstance(x, Boat): ...` type-checking |
| **Consistency** | Built-in functions like `len()`, `print()`, and operators like `+` behave predictably and uniformly across very different data types |

---

## Key Takeaways

- **Polymorphism** means "many forms" — the same function, method name, or operator behaves differently depending on the object it's used with.
- The built-in `len()` function is a simple, everyday example: it returns a character count for strings, item count for tuples/lists, and key/value pair count for dictionaries.
- **Class polymorphism**: unrelated classes (like `Car`, `Boat`, `Plane`) can each define a method with the same name (like `move()`), and you can call that method the same way on every object.
- **Inheritance polymorphism**: child classes inherit a parent's methods but can **override** them with their own version — Python automatically calls the correct version based on the object's actual class.
- **Duck typing** is why class polymorphism works without needing a shared parent class at all — Python only checks whether the method exists, not what type the object is.
- **Operators** (`+`, `-`, `==`, etc.) are polymorphic too, thanks to special dunder methods like `__add__()` behind the scenes.
- **Abstract classes** (via the `abc` module) let you *enforce* that every subclass implements a required method, which is useful in larger, more structured projects.
- **Overloading** (multiple methods, same name, different parameters) is **not** natively supported in Python — redefining a method just overwrites the previous one. Python developers fake it using default arguments, `*args`, or `functools.singledispatch`.
- **Overriding** (a subclass redefining a parent's method) **is** fully supported in Python and is resolved automatically using the Method Resolution Order (MRO) — Python always checks the object's own class before checking its parents. Use `super()` to call the parent's version from inside the override.
- The real payoff of polymorphism is **simpler, more reusable code**: write it once, and it works correctly across many different types of objects.
