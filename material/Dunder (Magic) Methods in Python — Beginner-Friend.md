<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Dunder (Magic) Methods in Python — Beginner-Friendly Guide

This note explains **dunder methods** (also called **magic methods**) in a simple way, with clear examples your students can run and modify.[^1][^2][^3][^4][^5][^6][^7][^8]

***

## What is a “dunder” method?

- **Dunder** = **Double UNDERscore**.
- A dunder method is a special method whose name starts and ends with **two underscores**, like:
    - `__init__`
    - `__str__`
    - `__repr__`
    - `__len__`
    - `__add__`
- You usually **don’t call them directly**. Python calls them **automatically** when you do certain operations (create an object, print it, use `len()`, use `+`, etc.).[^2][^3][^5][^6][^7][^8][^1]

Think of dunder methods as **hooks** that let your own classes behave like built-in types (like `list`, `str`, `int`).[^9][^10][^11][^1]

***

## Why do we use dunder methods?

They let you control how your objects:

- Are **created** and initialized
- Look when **printed** or inspected
- Behave with **operators** like `+`, `-`, `==`, `<`
- Work with built-in functions like `len()`, `iter()`, `str()`, `repr()`[^4][^5][^6][^8][^1][^2]

This makes your classes feel **natural** and **Pythonic**.

***

## The most important dunder methods for beginners

We’ll focus on the ones you’ll actually use a lot.[^5][^6][^1][^2][^4]

### 1) `__init__` — initialize a new object

**When is it called?**
When you create a new object: `obj = MyClass(...)`.

**What is it for?**
Set up the initial state of the object (assign attributes).

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Ali", 20)
print(s.name)  # Ali
print(s.age)   # 20
```

- `__init__` runs **automatically** when `Student("Ali", 20)` is executed.[^3][^7][^12][^13][^1][^2][^5]

***

### 2) `__str__` — human-friendly string (for users)

**When is it called?**
When you do:

- `print(obj)`
- `str(obj)`
- Use `f"{obj}"` in an f-string

**What is it for?**
Return a **readable** string for normal users.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student: {self.name}, {self.age} years old"

s = Student("Ali", 20)
print(s)          # Student: Ali, 20 years old
print(str(s))     # Student: Ali, 20 years old
msg = f"Info: {s}"
print(msg)        # Info: Student: Ali, 20 years old
```

If you don’t define `__str__`, Python uses `__repr__` instead.[^6][^11][^12][^13][^14][^1][^2][^3][^5]

***

### 3) `__repr__` — developer-friendly string (for debugging)

**When is it called?**

- In the interactive shell (REPL) when you type the variable name
- Inside lists/dicts when you print them
- When you call `repr(obj)`

**What is it for?**
Return an **unambiguous** string, ideally something that could help a developer recreate the object.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age!r})"

s = Student("Ali", 20)
print(repr(s))
# Student(name='Ali', age=20)

print([s])
# [Student(name='Ali', age=20)]
```

Rule of thumb for beginners:

- `__str__` → **nice for users** (`print`)
- `__repr__` → **useful for developers** (debugging, logs)[^10][^11][^13][^14][^1][^2][^5][^6]

***

### 4) `__len__` — make `len(obj)` work

**When is it called?**
When you call `len(obj)`.

**What is it for?**
Tell Python how many “items” your object has.

```python
class Team:
    def __init__(self, members):
        self.members = members  # list of names

    def __len__(self):
        return len(self.members)

team = Team(["Ali", "Sara", "Omar"])
print(len(team))  # 3
```

Now `Team` behaves like a container for `len()`.[^11][^14][^1][^2][^4][^5][^6]

***

### 5) `__eq__` — define equality (`==`)

**When is it called?**
When you write `obj1 == obj2`.

**What is it for?**
Define when two objects are considered **equal**.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.name == other.name and self.age == other.age

s1 = Student("Ali", 20)
s2 = Student("Ali", 20)
s3 = Student("Ali", 21)

print(s1 == s2)  # True
print(s1 == s3)  # False
```

Without `__eq__`, Python compares by **identity** (same object in memory), not by content.[^8][^2][^5][^6][^10]

***

### 6) `__add__` — define addition (`+`)

**When is it called?**
When you write `obj1 + obj2`.

**What is it for?**
Define what “adding” two objects means.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Vector(4, 6)
```

You can similarly define `__sub__`, `__mul__`, etc., for other operators.[^2][^5][^6][^11]

***

## A complete beginner example combining several dunder methods

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age} years old)"

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age!r})"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.name == other.name and self.age == other.age

s1 = Student("Ali", 20)
s2 = Student("Ali", 20)
s3 = Student("Sara", 22)

print(s1)           # Ali (20 years old)          -> uses __str__
print(repr(s1))     # Student(name='Ali', age=20) -> uses __repr__
print(s1 == s2)     # True                        -> uses __eq__
print(s1 == s3)     # False
```

This shows how dunder methods make your class **work nicely** with `print`, `repr`, and `==`.[^13][^1][^3][^5][^6][^2]

***

## Common dunder methods cheat sheet (beginner level)

| Dunder method | Triggered by | Typical use |
| :-- | :-- | :-- |
| `__init__` | `MyClass(...)` | Initialize new objects |
| `__str__` | `print(obj)`, `str(obj)` | User-friendly string representation |
| `__repr__` | `repr(obj)`, REPL, lists | Developer-friendly representation |
| `__len__` | `len(obj)` | Return number of items |
| `__eq__` | `obj1 == obj2` | Define equality |
| `__add__` | `obj1 + obj2` | Define addition |

You don’t need to memorize all dunder methods; start with these and add more as needed.[^1][^4][^5][^6][^8][^2]

***

## How to explain this to your students (simple story)

- A **class** is like a blueprint for objects.
- **Dunder methods** are special rules you write inside the class so Python knows:
    - How to **create** the object (`__init__`)
    - How to **show** it as text (`__str__`, `__repr__`)
    - How to **compare** it (`__eq__`)
    - How to **measure** it (`__len__`)
    - How to **combine** it with others (`__add__`)

You can tell them:
> “You don’t call these methods yourself. Python calls them automatically when you do normal things like `print`, `len`, or `+`. You just define them, and Python uses them behind the scenes.”[^7][^12][^3][^6][^8][^1]

***

If you’d like, I can generate a separate **exercise sheet** (with small tasks for students to implement `__str__`, `__repr__`, `__len__`, `__eq__` on their own classes) to go with this explanation.[^4][^1][^2]
<span style="display:none">[^15]</span>

<div align="center">⁂</div>

[^1]: https://algomaster.io/learn/python/dunder-methods

[^2]: https://blogs.eduarn.com/2026/07/dunder-methods-python-magic-methods-guide.html

[^3]: https://www.thenerdnook.io/p/python-day-19

[^4]: https://codegym.cc/groups/posts/python-magic-methods-dunders

[^5]: https://www.tutorialspoint.com/article/dunder-or-magic-methods-in-python

[^6]: https://generalistprogrammer.com/tutorials/python-magic-methods-dunder-complete-guide

[^7]: https://pythonprohub.com/advanced-python/python-dunder-methods-init-str-guide/

[^8]: https://zerotomastery.io/blog/python-dunder-methods/

[^9]: https://edgepython.com/language/dunders

[^10]: https://www.pykit.org/dunder-methods-demystified-making-your-python-classes-feel-built-in/

[^11]: https://thecodex.expert/coding/languages/python/python-data-model/

[^12]: https://dev.to/esthernaisimoi/python-helperdundermagic-methods-15bj

[^13]: https://logicdecode.in/blog/python-inheritance

[^14]: https://www.scribd.com/document/977897469/oop-lec3-p1

[^15]: https://www.geeksforgeeks.org/python/dunder-magic-methods-python/

