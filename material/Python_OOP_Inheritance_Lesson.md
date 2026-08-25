# Object-Oriented Programming in Python  
## Focus: Inheritance

**Audience:** Students who know Python fundamentals (variables, collections, functions, control flow) but have never used classes.  
**Goal:** Build a solid foundation in OOP, then master inheritance deeply enough to read and design class hierarchies confidently.

---

## Part 1 — Introduction to OOP (~25%)

### 1.1 Why OOP Exists

Procedural code works until the data and the functions that operate on it grow out of control.

```python
# Procedural style – becomes painful quickly
user1_name = "Ali"
user1_email = "ali@example.com"
user1_active = True

user2_name = "Sara"
user2_email = "sara@example.com"
user2_active = False

def deactivate_user(name, email, active):
    print(f"Deactivating {name} <{email}>")
    return False

user1_active = deactivate_user(user1_name, user1_email, user1_active)
```

Problems that appear:

- Data and behavior live in separate places.
- Adding a new field (role, last_login, …) forces changes in many functions.
- Relationships between pieces of data are not explicit.
- Duplication grows with every new entity (Customer, Employee, Admin).

OOP’s core idea: **keep the data and the behavior that belongs to it together**.

```python
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.active = True

    def deactivate(self):
        print(f"Deactivating {self.name} <{self.email}>")
        self.active = False

u1 = User("Ali", "ali@example.com")
u1.deactivate()
# Output:
# Deactivating Ali <ali@example.com>
```

The object now owns both its state and the operations that change that state.

### 1.2 Class, Object, Instance

| Term       | Meaning                                      |
|------------|----------------------------------------------|
| Class      | Blueprint that defines attributes & methods  |
| Object     | Concrete entity created from a class         |
| Instance   | Synonym for object of a particular class     |

```python
class User:
    pass

u1 = User()
u2 = User()

print(type(u1))          # <class '__main__.User'>
print(u1 is u2)          # False
print(id(u1) == id(u2))  # False
```

- `User` is the class (one blueprint).
- `u1` and `u2` are two independent instances.
- They share the same type but have different identities.

### 1.3 `self` — The Mechanical Explanation

When you write:

```python
u1.deactivate()
```

Python does the equivalent of:

```python
User.deactivate(u1)
```

The instance is passed as the first argument. That is why every instance method must accept `self`.

```python
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

u = User("Ali")
u.greet()
# Output: Hello, I am Ali
```

`self` is only a convention, not a keyword. The name can be anything, but using anything other than `self` is strongly discouraged.

### 1.4 `__init__` Initializes, It Does Not Create

1. Python creates a new empty object (via `__new__`).
2. Then it calls `__init__` on that already-created object to set initial state.

```python
class User:
    def __init__(self, name):
        print(f"Initializing object id={id(self)}")
        self.name = name

u = User("Ali")
# Output:
# Initializing object id=...
```

Common mistake: believing `__init__` creates the object. It only initializes it.

### 1.5 Instance Attributes vs Class Attributes

```python
class User:
    platform = "WebApp"          # class attribute – shared

    def __init__(self, name):
        self.name = name         # instance attribute – unique per object

u1 = User("Ali")
u2 = User("Sara")

print(u1.name)       # Ali
print(u2.name)       # Sara
print(u1.platform)   # WebApp
print(User.platform) # WebApp

u1.platform = "Mobile"   # creates an instance attribute that shadows the class one
print(u1.platform)   # Mobile
print(u2.platform)   # WebApp
print(User.platform) # WebApp
```

Lookup order: instance `__dict__` → class → parent classes (MRO) → AttributeError.

### 1.6 Is Python Fully Object-Oriented?

Everything in Python is an object (numbers, strings, functions, modules, classes themselves). You can always call methods on them:

```python
print((42).bit_length())     # 6
print("hello".upper())       # HELLO
```

However, Python does **not** force you to write in an OOP style. Procedural and functional code are equally valid and often preferred for simple scripts. Python is multi-paradigm: fully object-oriented under the hood, but not OOP-only in practice.

---

## Part 2 — Inheritance (~75%)

### 2.1 Why Inheritance Exists

Without inheritance we repeat the same attributes and methods in every related class:

```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def deactivate(self):
        self.active = False

class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def deactivate(self):
        self.active = False
```

Both are users. Inheritance lets us extract the common part into a parent class.

### 2.2 Basic Single Inheritance & Attribute Lookup

```python
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.active = True

    def deactivate(self):
        self.active = False
        print(f"{self.name} deactivated")

class Customer(User):
    def place_order(self, amount: float):
        print(f"{self.name} placed order of ${amount}")

c = Customer("Ali", "ali@example.com")
c.deactivate()
c.place_order(99.90)

# Output:
# Ali deactivated
# Ali placed order of $99.9
```

Lookup steps for `c.deactivate()`:

1. Look in `Customer` → not found.
2. Look in `User` → found → call it with `self = c`.

### 2.3 Method Overriding

```python
class User:
    def get_role(self):
        return "user"

class Customer(User):
    def get_role(self):
        return "customer"

c = Customer("Ali", "ali@example.com")
print(c.get_role())
# Output: customer
```

The child version is found first and used. This is the foundation of polymorphism.

### 2.4 `super()` — Continues Along the MRO

`super()` does **not** mean “call my direct parent”.  
It means “continue the search at the next class in the Method Resolution Order of the actual instance”.

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Customer(User):
    def __init__(self, name, email, loyalty_points=0):
        super().__init__(name, email)   # continues to User
        self.loyalty_points = loyalty_points

c = Customer("Ali", "ali@example.com", 150)
print(c.name, c.loyalty_points)
# Output: Ali 150
```

### 2.5 The Five Types of Inheritance

#### 2.5.1 Single Inheritance

One parent → one child.

```
User
  │
Customer
```

```python
class User:
    def __init__(self, name):
        self.name = name

class Customer(User):
    def __init__(self, name, cart_total=0.0):
        super().__init__(name)
        self.cart_total = cart_total

c = Customer("Ali", 49.99)
print(c.name, c.cart_total)
# Output: Ali 49.99
```

**Real-world use:** Any specialized user, product, or document type that shares a common base.

**Common mistake:** Forgetting `super().__init__()` and leaving parent attributes uninitialized.

#### 2.5.2 Multilevel Inheritance

Grandparent → parent → child.

```
User
  │
Employee
  │
Manager
```

```python
class User:
    def __init__(self, name):
        self.name = name

class Employee(User):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

m = Manager("Sara", "E-42", 8)
print(m.name, m.employee_id, m.team_size)
# Output: Sara E-42 8
```

**Real-world use:** Role hierarchies (User → Staff → Admin), document versions, vehicle categories.

**Common mistake:** Assuming attributes from the grandparent are automatically visible without proper `super()` chain.

#### 2.5.3 Hierarchical Inheritance

One parent → many children.

```
      User
     /    \
Customer  Employee
```

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Customer(User):
    def __init__(self, name, email, loyalty_points=0):
        super().__init__(name, email)
        self.loyalty_points = loyalty_points

class Employee(User):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.employee_id = employee_id

c = Customer("Ali", "ali@example.com", 200)
e = Employee("Sara", "sara@example.com", "E-7")
print(c.loyalty_points, e.employee_id)
# Output: 200 E-7
```

**Real-world use:** Different user roles, different payment methods, different product types.

**Common mistake:** Putting role-specific logic into the parent instead of the children.

#### 2.5.4 Multiple Inheritance

Child inherits from two or more parents.

```
  Logger          TimestampMixin
      \                /
       \              /
        ReportGenerator
```

```python
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class TimestampMixin:
    def timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()

class ReportGenerator(Logger, TimestampMixin):
    def generate(self, title):
        self.log(f"Generating report: {title} at {self.timestamp()}")

r = ReportGenerator()
r.generate("Sales Q3")
# Output:
# [LOG] Generating report: Sales Q3 at 2026-...
```

**Real-world use:** Mixins (logging, permissions, serialization) that add orthogonal behavior.

**Common mistake:** Assuming left-to-right order alone decides which method is called (MRO is more precise).

#### 2.5.5 Hybrid Inheritance

Any combination of the above (often multilevel + multiple).

```
      BaseService
       /       \
  AuthMixin   LoggingMixin
       \       /
     PaymentService
```

```python
class BaseService:
    def execute(self):
        print("Base execution")

class AuthMixin:
    def authenticate(self):
        print("Authenticated")

class LoggingMixin:
    def log(self, msg):
        print(f"LOG: {msg}")

class PaymentService(BaseService, AuthMixin, LoggingMixin):
    def process_payment(self, amount):
        self.authenticate()
        self.log(f"Processing ${amount}")
        self.execute()

p = PaymentService()
p.process_payment(49.99)
# Output:
# Authenticated
# LOG: Processing $49.99
# Base execution
```

**Real-world use:** Complex services that need authentication, logging, caching, etc., without deep single-inheritance trees.

### 2.6 Method Resolution Order (MRO)

Every class stores a linear list of classes Python will search.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
#  <class '__main__.A'>, <class 'object'>]
```

Search always starts at the instance’s class and follows this list until the attribute is found.

### 2.7 The Diamond Problem & C3 Linearization

```
    A
   / \
  B   C
   \ /
    D
```

Without a rule, `A` could be visited twice or in an ambiguous order. Python’s C3 linearization produces a consistent order that:

- respects local parent order,
- keeps each class only once,
- places children before parents.

```python
class A:
    def process(self):
        print("A")

class B(A):
    def process(self):
        print("B")
        super().process()

class C(A):
    def process(self):
        print("C")
        super().process()

class D(B, C):
    def process(self):
        print("D")
        super().process()

D().process()
# Actual output:
# D
# B
# C
# A
```

`super()` follows the MRO (`D → B → C → A → object`), not the direct parent of each class.

### 2.8 `isinstance()` vs `issubclass()`

```python
class User: pass
class Customer(User): pass

c = Customer()

print(isinstance(c, Customer))  # True
print(isinstance(c, User))      # True
print(issubclass(Customer, User))  # True
print(issubclass(User, Customer))  # False
```

- `isinstance(obj, cls)` — is this object an instance of cls or any subclass?
- `issubclass(cls, parent)` — is this class a subclass of parent?

### 2.9 Inheritance vs Composition (IS-A vs HAS-A)

| Relationship | Use when…                          | Example                     |
|--------------|------------------------------------|-----------------------------|
| IS-A (inheritance) | The child is a specialized kind of the parent | Customer is a User         |
| HAS-A (composition) | The object owns or uses another object | Order has a list of Products |

```python
# Inheritance (IS-A)
class User:
    def __init__(self, name):
        self.name = name

class Customer(User):
    pass

# Composition (HAS-A)
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()   # Car has an Engine

    def start(self):
        self.engine.start()

car = Car()
car.start()
# Output: Engine started
```

Prefer composition when the relationship is not a true “is-a” or when inheritance would create deep, fragile hierarchies.

### 2.10 Three Common Inheritance Mistakes

**Mistake 1 – Forgetting `super().__init__()`**

```python
# Wrong
class Customer(User):
    def __init__(self, name, email, points):
        self.points = points          # name and email never set

# Correct
class Customer(User):
    def __init__(self, name, email, points):
        super().__init__(name, email)
        self.points = points
```

**Mistake 2 – Believing `super()` always calls the direct parent**

In multiple inheritance `super()` follows the full MRO. Always inspect `Class.mro()` when the behavior surprises you.

**Mistake 3 – Using inheritance for a HAS-A relationship**

```python
# Wrong – Car is not an Engine
class Car(Engine):
    pass

# Correct
class Car:
    def __init__(self):
        self.engine = Engine()
```

---

## Practice Tasks (easiest → hardest)

1. Create a `Product` class with `name` and `price`. Add a method `display()`.
2. Create a `DigitalProduct` that inherits from `Product` and adds a `download_url`.
3. Build a three-level hierarchy: `Person` → `Employee` → `Manager`. Each level adds one attribute.
4. Create two sibling classes `Invoice` and `Receipt` that both inherit from `Document`.
5. Write a class that inherits from two mixins (`Serializable` and `Loggable`) and uses methods from both.
6. Design a small hybrid hierarchy that mixes multilevel and multiple inheritance; print its MRO.
7. Override a method in a child class and also call the parent version with `super()`.
8. Predict the output of a diamond-inheritance `super()` chain, then verify with code.
9. Refactor a class that incorrectly inherits into a composition design.
10. Implement a tiny payment system (`Payment` → `CreditCardPayment`, `PayPalPayment`) that uses overriding and polymorphism.

---

## Mental Model Summary

```
Class (blueprint)
        │
        ▼ creates
Object / Instance
        │
        ├── owns state (instance attributes)
        └── exposes behavior (methods)
                │
                └── self = the instance that was called
                        │
                        ▼
                 Inheritance (IS-A)
                        │
                        ├── reuses parent attributes & methods
                        ├── can override methods
                        └── super() continues along the MRO
                                │
                                ▼
                 Prefer Composition (HAS-A)
                 when the relationship is ownership, not specialization
```

Students who leave with this mental model can read real class hierarchies, predict method lookup, and choose between inheritance and composition deliberately.
