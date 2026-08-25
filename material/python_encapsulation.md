# Python Encapsulation — A Complete Guide

## Table of Contents
1. [What is Encapsulation?](#what-is-encapsulation)
2. [Levels of Access Control](#levels-of-access-control)
3. [Public Properties](#public-properties)
4. [Protected Properties](#protected-properties)
5. [Private Properties](#private-properties)
6. [Getter and Setter Methods](#getter-and-setter-methods)
7. [The `@property` Decorator (Pythonic Encapsulation)](#the-property-decorator-pythonic-encapsulation)
8. [Private Methods](#private-methods)
9. [Name Mangling Explained](#name-mangling-explained)
10. [Why Use Encapsulation?](#why-use-encapsulation)
11. [Full Example: Bank Account](#full-example-bank-account)
12. [Encapsulation vs Other OOP Concepts](#encapsulation-vs-other-oop-concepts)
13. [Key Takeaways](#key-takeaways)

---

## What is Encapsulation?

**Encapsulation** is one of the four core principles of Object-Oriented Programming (alongside Abstraction, Inheritance, and Polymorphism).

It means bundling data (attributes/properties) and the methods that operate on that data together inside a single class, while **controlling how that data can be accessed or modified from outside the class**.

In short: encapsulation hides an object's internal state and only exposes what's necessary through a controlled interface.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # hidden internal state
```

The goal isn't to make data completely inaccessible — it's to make sure it's accessed *deliberately*, through methods that can validate, transform, or log changes, rather than being modified carelessly from anywhere in the codebase.

---

## Levels of Access Control

Python doesn't have true `private`/`protected`/`public` keywords like Java or C++. Instead, it uses **naming conventions** to signal intent:

| Level | Syntax | Enforced by Python? | Meaning |
|---|---|---|---|
| Public | `self.name` | N/A | Freely accessible from anywhere |
| Protected | `self._name` | No (convention only) | "Internal use — subclasses may use this, but treat with care" |
| Private | `self.__name` | Partially (via name mangling) | "Do not access directly from outside the class" |

---

## Public Properties

By default, all attributes and methods in Python are public — accessible from anywhere, inside or outside the class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 25)
print(p1.name)  # Emil — freely accessible
p1.age = 30     # freely modifiable, no validation at all
```

This is fine for simple data, but it means nothing stops invalid values (`p1.age = -50`) or accidental overwrites.

---

## Protected Properties

A single leading underscore `_` marks an attribute as **protected** — a convention meaning "internal use, but subclasses are welcome to use it."

```python
class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary)  # Accessible, but shouldn't be touched directly
```

> **Note:** This is purely a convention. Python does **not** enforce it — you *can* access `_salary` from outside the class, but doing so signals you're bypassing the intended interface. Other developers (and linters) will treat this as a code smell.

Protected members are commonly used in inheritance, where a subclass legitimately needs access to a parent's internal state:

```python
class Employee(Person):
    def give_raise(self, amount):
        self._salary += amount  # subclass accessing protected attribute
```

---

## Private Properties

A **double** leading underscore `__` (with no more than one trailing underscore) makes a property private, triggering **name mangling** (explained below), which makes it much harder — though not impossible — to access from outside the class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private property

p1 = Person("Emil", 25)
print(p1.name)     # Emil
print(p1.__age)    # AttributeError: 'Person' object has no attribute '__age'
```

Private properties **cannot** be accessed directly from outside the class using the plain name. This is Python's closest equivalent to true data hiding.

---

## Getter and Setter Methods

Since private properties can't be accessed directly, the traditional approach is to provide explicit **getter** and **setter** methods.

### Getter — read a private value

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())  # 25
```

### Setter — write a private value, with validation

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())   # 25

p1.set_age(26)
print(p1.get_age())   # 26

p1.set_age(-5)         # Age must be positive (rejected)
```

This pattern gives you a **choke point**: every read and write goes through code you control, so you can validate, log, transform, or restrict changes.

---

## The `@property` Decorator (Pythonic Encapsulation)

Explicit `get_x()` / `set_x()` methods work, but Python offers a cleaner, more idiomatic way to achieve the same encapsulation using the built-in `@property` decorator. This lets you keep the **simple attribute-style syntax** (`p1.age`) on the outside, while still running validation code underneath.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):          # acts as the getter
        return self.__age

    @age.setter
    def age(self, value):   # acts as the setter
        if value > 0:
            self.__age = value
        else:
            raise ValueError("Age must be positive")

    @age.deleter
    def age(self):           # acts as the deleter
        print("Deleting age...")
        del self.__age


p1 = Person("Tobias", 25)
print(p1.age)     # 25 — looks like direct attribute access, but calls the getter
p1.age = 30       # calls the setter, validates automatically
print(p1.age)     # 30

p1.age = -5       # raises ValueError: Age must be positive
```

This is considered the more **Pythonic** approach because:
- The external interface still *looks* like a simple attribute (`p1.age`), not a method call (`p1.get_age()`).
- You can start with plain public attributes and **add validation later** using `@property`, without breaking any code that already uses `obj.age`.
- It follows Python's philosophy: "we're all consenting adults here" — encapsulation is about clear structure and safety nets, not building an impenetrable wall.

---

## Private Methods

Just like properties, methods can be marked private using a double underscore prefix. This is typically used for internal helper logic that shouldn't be called from outside the class.

```python
class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        return True

    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)     # 15

# calc.__validate(5)   # AttributeError — private methods aren't accessible directly
```

`__validate` is an implementation detail. Users of `Calculator` only need to know about `add()` — how it validates input internally is none of their concern. This keeps the public interface minimal and stable, even if the internal validation logic changes later.

---

## Name Mangling Explained

**Name mangling** is the actual mechanism Python uses to implement "private" members. It's not true privacy — it's a renaming trick that makes accidental access unlikely.

When you write an attribute or method with a double-underscore prefix (and at most one trailing underscore) inside a class body, Python automatically renames it internally to:

```
_ClassName__attributeName
```

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

p1 = Person("Emil", 30)

# This is how Python actually stores it internally:
print(p1._Person__age)  # 30 — technically accessible!
```

So `__age` isn't truly hidden — it's just renamed to `_Person__age`, and Python translates every reference to `self.__age` *inside the class* into `self._Person__age` automatically. From outside the class, you'd need to know and use that mangled name, which discourages (but doesn't prevent) direct access.

> **Why does mangling exist?** Its original purpose is to avoid naming collisions in inheritance — if a parent class and child class both define `__value`, mangling ensures they don't accidentally overwrite each other, since they become `_Parent__value` and `_Child__value` respectively.

```python
class Base:
    def __init__(self):
        self.__value = "base"

    def show_base(self):
        return self.__value   # refers to _Base__value

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__value = "child"   # this is a DIFFERENT attribute: _Child__value

    def show_child(self):
        return self.__value      # refers to _Child__value

c = Child()
print(c.show_base())    # base
print(c.show_child())   # child
```

Without mangling, `Child.__value` would silently overwrite `Base.__value`, which could break the parent class's internal logic.

> **Best practice:** Accessing the mangled name directly (`obj._ClassName__attr`) works, but it defeats the entire purpose of encapsulation. Treat it as a debugging tool at most — never as part of your program's normal logic.

---

## Why Use Encapsulation?

| Benefit | Explanation |
|---|---|
| **Data Protection** | Prevents attributes from being changed carelessly or inconsistently from arbitrary places in the code |
| **Validation** | Setters (or `@property` setters) can reject invalid values before they're ever stored |
| **Flexibility** | The internal implementation can change freely (e.g., switching from a single value to a computed one) without breaking external code that uses the same interface |
| **Control** | The class author decides exactly how, when, and whether data can be read or modified |
| **Debuggability** | Since all mutations flow through a small set of methods, it's much easier to trace where and why a value changed |
| **Encourages loose coupling** | External code depends on the *interface* (`get_age()`, `obj.age`), not on internal representation, so classes can evolve independently |

---

## Full Example: Bank Account

A more real-world example that ties private state, validation, and a clean public interface together:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance          # private: no direct external access
        self.__transaction_log = []       # private: internal record-keeping

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self.__transaction_log.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.__transaction_log.append(f"Withdrew {amount}")

    def __validate_pin(self, pin):
        return pin == 1234   # private helper, internal logic only

    def get_statement(self):
        return "\n".join(self.__transaction_log)


account = BankAccount("Sara", 100)
account.deposit(50)
account.withdraw(30)

print(account.balance)         # 120 — via @property getter, read-only from outside
print(account.get_statement()) # Deposited 50 \n Withdrew 30

# account.balance = 999        # AttributeError: no setter defined -> read-only property
# account.__balance             # not the real attribute; would need account._BankAccount__balance
```

Notice that `balance` here is exposed as **read-only** (no `@balance.setter` defined) — the only way to change it is through `deposit()` and `withdraw()`, which enforce the account's business rules. This is encapsulation doing real work: it's not just about hiding data, it's about **protecting the account's rules from being bypassed**.

---

## Encapsulation vs Other OOP Concepts

It helps to see how encapsulation relates to the other pillars of OOP:

| Concept | What it does | Example |
|---|---|---|
| **Encapsulation** | Bundles data + behavior, controls access to internal state | `__balance`, `get_age()`, `@property` |
| **Abstraction** | Hides *complexity*, exposes only relevant behavior (a broader idea than encapsulation) | Abstract base classes, exposing `area()` without exposing the math inside |
| **Inheritance** | Reuses and extends behavior from a parent class | `class Dog(Animal)` |
| **Polymorphism** | Same interface, different behavior depending on the object's type | `len(obj)`, method overriding |

Encapsulation and abstraction are closely related and often confused: encapsulation is about **restricting access** to implementation details, while abstraction is about **simplifying** what's exposed to the user, regardless of access level.

---

## Key Takeaways

- Encapsulation bundles data and methods together and **controls access** to that data from outside the class.
- Python has no true `private` keyword — it uses **naming conventions**: `_protected` (convention only) and `__private` (enforced via name mangling).
- **Name mangling** rewrites `__attr` to `_ClassName__attr`, which discourages — but doesn't fully prevent — outside access.
- **Getter/setter methods** (`get_age()`/`set_age()`) are the traditional way to control access to private data, allowing validation.
- The **`@property` decorator** is the more Pythonic approach: it lets you keep clean attribute-style syntax (`obj.age`) while still running getter/setter logic underneath.
- Private methods (`__validate()`) hide internal implementation details, keeping the class's public interface small and stable.
- Encapsulation's real value isn't secrecy — it's **safety, validation, and the freedom to change internal implementation** without breaking external code.
