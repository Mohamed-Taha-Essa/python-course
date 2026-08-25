# Python Dictionaries — Complete Guide
## From Beginner to Advanced

A professional teaching guide for explaining Python `dict` from the basics to advanced usage, with practical and real-world examples.

---

## 1. What Is a Dictionary?

A Python dictionary (`dict`) is a **mutable mapping of unique keys to values**.

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "grade": 85,
}
```

Think of it as:

```text
key       -> value
"name"    -> "Ahmed"
"age"     -> 20
"grade"   -> 85
```

Dictionaries are especially useful when data has a meaningful identifier:

```python
user_id -> user
product_id -> product
username -> profile
course -> students
word -> count
```

---

## 2. Why Use Dictionaries?

Compare a list:

```python
user = ["Ahmed", 20, "Cairo"]
```

with a dictionary:

```python
user = {
    "name": "Ahmed",
    "age": 20,
    "city": "Cairo",
}
```

The dictionary makes the meaning explicit:

```python
print(user["name"])
print(user["age"])
```

This is one of the reasons dictionaries are fundamental in backend development, APIs, configuration, and JSON processing.

---

# 3. Creating Dictionaries

## Empty dictionary

```python
data = {}
```

or:

```python
data = dict()
```

## Dictionary with data

```python
student = {
    "name": "Ali",
    "age": 21,
    "city": "Cairo",
}
```

## Using `dict()`

```python
student = dict(
    name="Ali",
    age=21,
    city="Cairo",
)
```

---

# 4. Dictionary Keys

Keys must be **hashable**.

Valid examples:

```python
data = {
    "name": "Ali",
    1: "one",
    3.14: "pi",
    True: "yes",
    (1, 2): "tuple key",
}
```

Invalid:

```python
data = {
    [1, 2]: "list key",
}
```

This raises:

```text
TypeError: unhashable type: 'list'
```

Why? Lists are mutable and therefore cannot be used as normal dictionary keys.

---

# 5. Keys Must Be Unique

```python
student = {
    "name": "Ali",
    "age": 20,
    "name": "Ahmed",
}
```

The last `"name"` replaces the previous one:

```python
{
    "name": "Ahmed",
    "age": 20,
}
```

A dictionary cannot keep two separate values under the same key.

---

# 6. Dictionary Values

Values can be almost any Python object:

```python
student = {
    "name": "Ali",
    "age": 20,
    "active": True,
    "skills": ["Python", "Django"],
    "address": {
        "city": "Cairo",
        "country": "Egypt",
    },
}
```

Values can therefore be:

- strings
- numbers
- booleans
- `None`
- lists
- tuples
- sets
- dictionaries
- custom objects

---

# 7. Accessing Values

Use:

```python
student["name"]
```

Example:

```python
student = {
    "name": "Ali",
    "age": 20,
}

print(student["name"])
```

Output:

```text
Ali
```

---

# 8. Missing Keys and `KeyError`

This:

```python
print(student["email"])
```

raises:

```text
KeyError: 'email'
```

This is one of the most common dictionary errors.

---

# 9. The `get()` Method

## Syntax

```python
dictionary.get(key, default=None)
```

Example:

```python
student = {
    "name": "Ali",
    "age": 20,
}

print(student.get("name"))
print(student.get("email"))
```

Output:

```text
Ali
None
```

Custom default:

```python
print(student.get("email", "Not provided"))
```

Output:

```text
Not provided
```

### `[]` vs `get()`

Use:

```python
student["email"]
```

when the key is required.

Use:

```python
student.get("email")
```

when the key may be absent.

---

# 10. Adding a Key

```python
student = {
    "name": "Ali",
    "age": 20,
}

student["city"] = "Cairo"
```

Now:

```python
{
    "name": "Ali",
    "age": 20,
    "city": "Cairo",
}
```

---

# 11. Updating a Value

```python
student["age"] = 21
```

If the key exists, its value changes.

If it does not exist, the key is created.

---

# 12. `update()`

`update()` adds or replaces multiple key-value pairs.

```python
student = {
    "name": "Ali",
    "age": 20,
}

student.update({
    "age": 21,
    "city": "Cairo",
})
```

Result:

```python
{
    "name": "Ali",
    "age": 21,
    "city": "Cairo",
}
```

It can also accept keyword arguments:

```python
student.update(
    city="Giza",
    job="Developer",
)
```

---

# 13. `setdefault()`

`setdefault()` gets a value if the key exists. Otherwise it creates the key with a default.

```python
user = {
    "name": "Ali",
}

age = user.setdefault("age", 20)

print(age)
print(user)
```

Result:

```python
20
{'name': 'Ali', 'age': 20}
```

If the key already exists:

```python
user = {
    "name": "Ali",
    "age": 25,
}

age = user.setdefault("age", 20)

print(age)
```

Result:

```text
25
```

The existing value is not replaced.

---

# 14. Removing Dictionary Data

There are four important techniques:

```python
del
pop()
popitem()
clear()
```

---

# 15. `del`

```python
student = {
    "name": "Ali",
    "age": 20,
    "city": "Cairo",
}

del student["city"]
```

Now:

```python
{
    "name": "Ali",
    "age": 20,
}
```

A missing key causes `KeyError`.

---

# 16. `pop()`

`pop()` removes a key and returns its value.

```python
student = {
    "name": "Ali",
    "age": 20,
}

age = student.pop("age")

print(age)
print(student)
```

Output:

```text
20
{'name': 'Ali'}
```

Default value:

```python
email = student.pop("email", "Not found")
```

---

# 17. `popitem()`

`popitem()` removes and returns the **last inserted key-value pair**.

```python
student = {
    "name": "Ali",
    "age": 20,
    "city": "Cairo",
}

item = student.popitem()

print(item)
```

Output:

```text
('city', 'Cairo')
```

The returned value is a tuple.

---

# 18. `clear()`

Removes all items.

```python
student.clear()
```

Result:

```python
{}
```

---

# 19. Checking Keys With `in`

```python
student = {
    "name": "Ali",
    "age": 20,
}

print("name" in student)
print("email" in student)
```

Output:

```text
True
False
```

Important:

```python
"name" in student
```

checks keys.

---

# 20. Checking Values

Use `.values()`:

```python
print("Ali" in student.values())
```

Example:

```python
student = {
    "name": "Ali",
    "city": "Cairo",
}

print("Cairo" in student.values())
```

---

# 21. `keys()`

Returns a dynamic view of the keys.

```python
student.keys()
```

Example:

```python
print(student.keys())
```

Typical output:

```text
dict_keys(['name', 'city'])
```

Loop:

```python
for key in student.keys():
    print(key)
```

Usually this is enough:

```python
for key in student:
    print(key)
```

---

# 22. `values()`

Returns a dynamic view of values.

```python
print(student.values())
```

Example:

```python
for value in student.values():
    print(value)
```

---

# 23. `items()`

Returns key-value pairs.

```python
print(student.items())
```

Typical output:

```text
dict_items([('name', 'Ali'), ('city', 'Cairo')])
```

This is the standard way to iterate through both keys and values:

```python
for key, value in student.items():
    print(key, value)
```

---

# 24. Dictionary Views

`keys()`, `values()`, and `items()` return **view objects**, not regular lists.

Example:

```python
user = {
    "name": "Ali",
}

keys = user.keys()

user["age"] = 20

print(keys)
```

The view reflects the current dictionary.

Convert to lists when needed:

```python
list(user.keys())
list(user.values())
list(user.items())
```

---

# 25. `copy()`

Creates a **shallow copy**.

```python
user = {
    "name": "Ali",
    "age": 20,
}

user_copy = user.copy()

user_copy["age"] = 30

print(user)
print(user_copy)
```

The top-level dictionaries are separate.

---

# 26. Assignment vs Copy

Assignment:

```python
user1 = {
    "name": "Ali",
}

user2 = user1

user2["name"] = "Ahmed"

print(user1)
```

Output:

```python
{'name': 'Ahmed'}
```

Both names refer to the same dictionary.

Copy:

```python
user1 = {
    "name": "Ali",
}

user2 = user1.copy()

user2["name"] = "Ahmed"
```

Now:

```python
user1 == {"name": "Ali"}
user2 == {"name": "Ahmed"}
```

---

# 27. Shallow vs Deep Copy

Shallow copy:

```python
user = {
    "name": "Ali",
    "profile": {
        "city": "Cairo",
    },
}

user_copy = user.copy()

user_copy["profile"]["city"] = "Giza"

print(user["profile"]["city"])
```

The nested dictionary is still shared.

For an independent nested copy:

```python
import copy

user_copy = copy.deepcopy(user)
```

Now nested objects are copied as well.

---

# 28. `dict.fromkeys()`

Syntax:

```python
dict.fromkeys(iterable, value=None)
```

Example:

```python
keys = ["name", "age", "city"]

student = dict.fromkeys(keys)

print(student)
```

Result:

```python
{
    "name": None,
    "age": None,
    "city": None,
}
```

With a default:

```python
grades = dict.fromkeys(
    ["math", "english", "python"],
    0,
)
```

---

# 29. Important `fromkeys()` Warning

Avoid mutable defaults unless you intentionally want shared state.

```python
data = dict.fromkeys(
    ["a", "b", "c"],
    [],
)

data["a"].append(10)

print(data)
```

All keys refer to the same list.

Better:

```python
data = {
    key: []
    for key in ["a", "b", "c"]
}
```

---

# 30. Dictionary Order

Modern Python dictionaries preserve insertion order.

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3,
}
```

Iterating produces keys in insertion order:

```python
for key in data:
    print(key)
```

Output:

```text
a
b
c
```

Dictionary equality still depends on key-value content, not insertion order.

```python
{"a": 1, "b": 2} == {"b": 2, "a": 1}
```

is:

```text
True
```

---

# 31. Looping Through Dictionaries

## Keys

```python
for key in data:
    print(key)
```

## Values

```python
for value in data.values():
    print(value)
```

## Key + value

```python
for key, value in data.items():
    print(key, value)
```

---

# 32. Dictionary Comprehension

Basic:

```python
numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}
```

Result:

```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25,
}
```

---

# 33. Dictionary Comprehension With Condition

```python
numbers = range(1, 11)

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}
```

Result:

```python
{
    2: 4,
    4: 16,
    6: 36,
    8: 64,
    10: 100,
}
```

---

# 34. Transforming a Dictionary

```python
prices = {
    "apple": 10,
    "banana": 5,
    "orange": 12,
}

new_prices = {
    product: price * 1.10
    for product, price in prices.items()
}
```

---

# 35. Filtering a Dictionary

```python
prices = {
    "apple": 10,
    "banana": 5,
    "orange": 12,
}

expensive = {
    product: price
    for product, price in prices.items()
    if price > 8
}
```

Result:

```python
{
    "apple": 10,
    "orange": 12,
}
```

---

# 36. Nested Dictionaries

Real applications often contain nested structures.

```python
company = {
    "name": "Tech Company",
    "employees": {
        "manager": {
            "name": "Ahmed",
            "salary": 30000,
        },
        "developer": {
            "name": "Ali",
            "salary": 20000,
        },
    },
}
```

Access:

```python
company["employees"]["developer"]["name"]
```

---

# 37. Safe Nested Access

This can fail:

```python
city = user["profile"]["address"]["city"]
```

A safer approach:

```python
city = (
    user.get("profile", {})
        .get("address", {})
        .get("city")
)
```

This is common when processing incomplete API responses.

---

# 38. List of Dictionaries

Very common in APIs:

```python
users = [
    {
        "id": 1,
        "name": "Ahmed",
    },
    {
        "id": 2,
        "name": "Ali",
    },
]
```

Loop:

```python
for user in users:
    print(user["name"])
```

---

# 39. Filtering a List of Dictionaries

```python
users = [
    {"name": "Ahmed", "age": 30},
    {"name": "Ali", "age": 17},
    {"name": "Mona", "age": 25},
]

adults = [
    user
    for user in users
    if user["age"] >= 18
]
```

---

# 40. Sorting a List of Dictionaries

```python
users = [
    {"name": "Ahmed", "age": 30},
    {"name": "Ali", "age": 17},
    {"name": "Mona", "age": 25},
]

users.sort(key=lambda user: user["age"])
```

Descending:

```python
users.sort(
    key=lambda user: user["age"],
    reverse=True,
)
```

---

# 41. Counting With a Dictionary

Given:

```python
words = [
    "python",
    "java",
    "python",
    "django",
    "python",
    "java",
]
```

Create:

```python
{
    "python": 3,
    "java": 2,
    "django": 1,
}
```

Solution:

```python
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1
```

This is one of the most important dictionary patterns.

---

# 42. Grouping With `setdefault()`

```python
students = [
    ("Ahmed", "Python"),
    ("Ali", "Django"),
    ("Mona", "Python"),
    ("Omar", "Django"),
]

courses = {}

for name, course in students:
    courses.setdefault(course, []).append(name)
```

Result:

```python
{
    "Python": ["Ahmed", "Mona"],
    "Django": ["Ali", "Omar"],
}
```

---

# 43. `defaultdict`

For grouping, `collections.defaultdict` can be cleaner.

```python
from collections import defaultdict

courses = defaultdict(list)

students = [
    ("Ahmed", "Python"),
    ("Ali", "Django"),
    ("Mona", "Python"),
]

for name, course in students:
    courses[course].append(name)
```

---

# 44. Counting With `Counter`

For frequency counting:

```python
from collections import Counter

words = [
    "python",
    "java",
    "python",
    "django",
    "python",
    "java",
]

counts = Counter(words)

print(counts)
```

This is specialized for counting and adds methods such as:

```python
counts.most_common(2)
```

---

# 45. Sorting Dictionary Keys

```python
data = {
    "z": 1,
    "a": 2,
    "m": 3,
}

sorted(data)
```

Result:

```python
['a', 'm', 'z']
```

To create a sorted dictionary:

```python
sorted_data = dict(sorted(data.items()))
```

---

# 46. Sorting by Values

```python
scores = {
    "Ahmed": 90,
    "Ali": 80,
    "Mona": 95,
}

sorted_scores = dict(
    sorted(
        scores.items(),
        key=lambda item: item[1],
    )
)
```

Descending:

```python
sorted_scores = dict(
    sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True,
    )
)
```

---

# 47. Sorting With `itemgetter`

```python
from operator import itemgetter

sorted_scores = dict(
    sorted(
        scores.items(),
        key=itemgetter(1),
        reverse=True,
    )
)
```

---

# 48. Find Max and Min by Value

```python
scores = {
    "Ahmed": 90,
    "Ali": 80,
    "Mona": 95,
}

best_student = max(scores, key=scores.get)
worst_student = min(scores, key=scores.get)

print(best_student)
print(worst_student)
```

Output:

```text
Mona
Ali
```

---

# 49. `len()`

```python
user = {
    "name": "Ali",
    "age": 20,
}

print(len(user))
```

Returns the number of keys.

---

# 50. `list()`

```python
user = {
    "name": "Ali",
    "age": 20,
}

list(user)
list(user.keys())
list(user.values())
list(user.items())
```

---

# 51. `reversed()`

Dictionaries can be traversed in reverse insertion order.

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3,
}

print(list(reversed(data)))
```

Result:

```python
['c', 'b', 'a']
```

---

# 52. `sum()`, `min()`, `max()`

Important distinction:

```python
min(data)
max(data)
```

operate on keys.

For values:

```python
min(data.values())
max(data.values())
sum(data.values())
```

Example:

```python
grades = {
    "math": 90,
    "english": 80,
    "python": 95,
}

print(sum(grades.values()))
print(min(grades.values()))
print(max(grades.values()))
```

---

# 53. `any()` and `all()`

For values:

```python
data = {
    "a": True,
    "b": True,
}

print(any(data.values()))
print(all(data.values()))
```

- `any()` -> at least one truthy value.
- `all()` -> every value is truthy.

---

# 54. `enumerate()`

```python
users = {
    "u1": "Ahmed",
    "u2": "Ali",
    "u3": "Mona",
}

for index, key in enumerate(users):
    print(index, key)
```

---

# 55. `zip()` + `dict()`

A very useful pattern:

```python
names = ["Ahmed", "Ali", "Mona"]
grades = [90, 80, 95]

students = dict(zip(names, grades))
```

Result:

```python
{
    "Ahmed": 90,
    "Ali": 80,
    "Mona": 95,
}
```

If sequences have different lengths, `zip()` stops at the shortest one.

---

# 56. Dictionary Unpacking

Use `**`:

```python
base_user = {
    "name": "Ali",
}

extra_data = {
    "age": 20,
    "city": "Cairo",
}

user = {
    **base_user,
    **extra_data,
}
```

---

# 57. Duplicate Keys During Unpacking

The later value wins:

```python
a = {
    "name": "Ali",
    "age": 20,
}

b = {
    "age": 30,
}

result = {
    **a,
    **b,
}
```

Result:

```python
{
    "name": "Ali",
    "age": 30,
}
```

---

# 58. Dictionary Union `|`

Modern Python supports:

```python
a = {"name": "Ali"}
b = {"age": 20}

result = a | b
```

Result:

```python
{
    "name": "Ali",
    "age": 20,
}
```

The original dictionaries are unchanged.

---

# 59. In-Place Union `|=`

```python
user = {
    "name": "Ali",
}

user |= {
    "age": 20,
    "city": "Cairo",
}
```

This updates `user`.

For duplicate keys, the right side wins.

---

# 60. `update()` vs `|`

`update()` modifies the existing dictionary:

```python
a.update(b)
```

`|` creates a new dictionary:

```python
result = a | b
```

---

# 61. Dictionary Equality and Identity

Equality:

```python
a == b
```

checks content.

Identity:

```python
a is b
```

checks whether both names point to the exact same object.

Example:

```python
a = {"name": "Ali"}
b = a
c = a.copy()

print(a == b)  # True
print(a is b)  # True

print(a == c)  # True
print(a is c)  # False
```

---

# 62. JSON and Dictionaries

JSON objects naturally map to Python dictionaries.

JSON:

```json
{
    "name": "Ali",
    "age": 20
}
```

Python:

```python
{
    "name": "Ali",
    "age": 20,
}
```

Convert dictionary to JSON text:

```python
import json

data = {
    "name": "Ali",
    "age": 20,
}

json_text = json.dumps(data)
```

Convert JSON text to dictionary:

```python
data = json.loads(json_text)
```

---

# 63. Real Example: API Response

```python
response = {
    "status": "success",
    "data": {
        "user": {
            "id": 10,
            "name": "Mohamed",
        }
    },
}
```

Access:

```python
user_id = response["data"]["user"]["id"]
```

Safe access:

```python
name = (
    response
    .get("data", {})
    .get("user", {})
    .get("name")
)
```

---

# 64. Real Example: Product

```python
product = {
    "id": 1001,
    "name": "Office Chair",
    "price": 2500,
    "stock": 15,
    "category": {
        "id": 3,
        "name": "Chairs",
    },
    "tags": ["office", "chair", "furniture"],
}
```

Update price:

```python
product["price"] = 2700
```

Decrease stock:

```python
product["stock"] -= 1
```

Add a tag:

```python
product["tags"].append("comfortable")
```

---

# 65. Real Example: HTTP Headers

```python
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer TOKEN",
}
```

Dictionary use in networking often follows this style.

---

# 66. Real Example: Configuration

```python
config = {
    "DEBUG": True,
    "HOST": "127.0.0.1",
    "PORT": 8000,
}
```

Read:

```python
port = config["PORT"]
```

---

# 67. Real Example: Request Data Validation

```python
request_data = {
    "username": "mohamed",
    "email": "mohamed@example.com",
    "age": 30,
}

required_fields = [
    "username",
    "email",
]

for field in required_fields:
    if field not in request_data:
        print(f"Missing field: {field}")
```

---

# 68. Real Backend Example: Partial Update

```python
user = {
    "id": 1,
    "name": "Ali",
    "email": "ali@example.com",
    "active": True,
}

update_data = {
    "name": "Ahmed",
    "active": False,
}

user.update(update_data)
```

This is conceptually similar to processing partial update payloads.

---

# 69. Real Example: Student Payment System

```python
students = {
    101: {
        "name": "Ahmed",
        "monthly_payment": 500,
        "paid_months": ["January", "February"],
    },
    102: {
        "name": "Ali",
        "monthly_payment": 600,
        "paid_months": ["January"],
    },
}
```

Check student:

```python
student_id = 101

if student_id in students:
    print("Student found")
```

Check March payment:

```python
student = students.get(101)

if student:
    if "March" in student["paid_months"]:
        print("Already paid")
    else:
        print("Payment required")
```

Register March payment:

```python
student = students[101]

if "March" not in student["paid_months"]:
    student["paid_months"].append("March")
```

Calculate expected collected revenue:

```python
total_revenue = sum(
    student["monthly_payment"]
    * len(student["paid_months"])
    for student in students.values()
)
```

---

# 70. Real Example: Inventory

```python
inventory = {
    "chair": {
        "price": 2500,
        "stock": 10,
    },
    "desk": {
        "price": 5000,
        "stock": 5,
    },
}
```

Decrease stock:

```python
inventory["chair"]["stock"] -= 1
```

Check:

```python
if inventory["chair"]["stock"] > 0:
    print("Available")
```

Inventory value:

```python
total_value = sum(
    product["price"] * product["stock"]
    for product in inventory.values()
)
```

---

# 71. Lookup Tables

Dictionaries can replace long `if/elif` chains.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

operations = {
    "add": add,
    "subtract": subtract,
}

operation = "add"

result = operations[operation](10, 5)

print(result)
```

Output:

```text
15
```

This is called a dispatch table.

---

# 72. State Machine Example

```python
transitions = {
    "pending": "processing",
    "processing": "completed",
    "completed": "archived",
}

state = "pending"

state = transitions[state]
print(state)
```

---

# 73. Dictionary for Translations

```python
translations = {
    "welcome": {
        "en": "Welcome",
        "ar": "مرحبا",
    },
    "login": {
        "en": "Login",
        "ar": "تسجيل الدخول",
    },
}
```

Get Arabic:

```python
print(translations["welcome"]["ar"])
```

---

# 74. Building an Index for Fast Lookup

Suppose:

```python
products = [
    {"id": 101, "name": "Chair"},
    {"id": 102, "name": "Desk"},
    {"id": 103, "name": "Lamp"},
]
```

Build an index:

```python
product_by_id = {
    product["id"]: product
    for product in products
}
```

Now:

```python
product = product_by_id.get(102)
```

This is much more convenient for repeated identifier-based lookup than scanning the whole list each time.

---

# 75. Grouping Data

```python
orders = [
    {"customer": "Ahmed", "total": 100},
    {"customer": "Ali", "total": 200},
    {"customer": "Ahmed", "total": 150},
]
```

Group orders:

```python
grouped = {}

for order in orders:
    customer = order["customer"]
    grouped.setdefault(customer, []).append(order)
```

Result:

```python
{
    "Ahmed": [
        {"customer": "Ahmed", "total": 100},
        {"customer": "Ahmed", "total": 150},
    ],
    "Ali": [
        {"customer": "Ali", "total": 200},
    ],
}
```

---

# 76. Advanced: Recursive Flattening

Input:

```python
data = {
    "user": {
        "profile": {
            "name": "Ali",
            "city": "Cairo",
        }
    }
}
```

Desired shape:

```python
{
    "user.profile.name": "Ali",
    "user.profile.city": "Cairo",
}
```

Implementation:

```python
def flatten_dict(data, parent_key="", sep="."):
    result = {}

    for key, value in data.items():
        new_key = (
            f"{parent_key}{sep}{key}"
            if parent_key
            else str(key)
        )

        if isinstance(value, dict):
            result.update(
                flatten_dict(value, new_key, sep)
            )
        else:
            result[new_key] = value

    return result
```

---

# 77. Advanced: Recursive Search

```python
def find_key(data, target):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target:
                return value

            result = find_key(value, target)

            if result is not None:
                return result

    elif isinstance(data, list):
        for item in data:
            result = find_key(item, target)

            if result is not None:
                return result

    return None
```

This pattern can be used when exploring complex nested JSON-like structures.

---

# 78. Advanced: Deep Merge

The `|` operator performs a shallow merge.

```python
a = {
    "user": {
        "name": "Ali",
    }
}

b = {
    "user": {
        "age": 20,
    }
}

result = a | b
```

Result:

```python
{
    "user": {
        "age": 20,
    }
}
```

It does not recursively merge nested dictionaries.

A recursive merge can be implemented:

```python
def deep_merge(left, right):
    result = left.copy()

    for key, value in right.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value

    return result
```

---

# 79. Advanced: Dictionary Pattern Matching

Python supports structural pattern matching:

```python
def process_user(user):
    match user:
        case {"name": name, "age": age}:
            print(f"{name} is {age} years old")

        case {"name": name}:
            print(f"User: {name}")

        case _:
            print("Unknown structure")
```

Useful for structured input handling.

---

# 80. Type Hints

Basic:

```python
user: dict = {
    "name": "Ali",
    "age": 20,
}
```

More precise:

```python
scores: dict[str, int] = {
    "Ahmed": 90,
    "Ali": 80,
}
```

---

# 81. `TypedDict`

For dictionaries with a known schema:

```python
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
    active: bool
```

Usage:

```python
user: User = {
    "id": 1,
    "name": "Ali",
    "active": True,
}
```

This improves type checking in larger applications.

---

# 82. `dict` vs `dataclass`

Use a dictionary when:

- structure is flexible
- data comes from JSON/API input
- keys vary
- a lightweight mapping is enough

Use a class/dataclass when:

- structure is stable
- data has behavior/methods
- domain modeling matters
- you want stronger typing

Example:

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    active: bool
```

---

# 83. Hashing and Dictionary Keys

Keys must have a stable hash.

Examples:

```python
hash("hello")
hash(10)
hash((1, 2))
```

But:

```python
hash([1, 2])
```

raises:

```text
TypeError: unhashable type: 'list'
```

This explains why mutable objects such as lists cannot be dictionary keys.

---

# 84. Complexity

Average-case complexity for common operations:

| Operation | Average |
|---|---:|
| `d[key]` | O(1) |
| `d.get(key)` | O(1) |
| `key in d` | O(1) |
| `d[key] = value` | O(1) |
| `d.pop(key)` | O(1) |
| Iteration | O(n) |

Exact performance depends on implementation details and hash behavior, but dictionaries are designed for fast average lookup.

---

# 85. Modifying During Iteration

Avoid changing dictionary size during iteration:

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for key in data:
    if key == "b":
        del data[key]
```

This can raise:

```text
RuntimeError: dictionary changed size during iteration
```

Safer:

```python
for key in list(data):
    if key == "b":
        del data[key]
```

Or use a comprehension:

```python
data = {
    key: value
    for key, value in data.items()
    if key != "b"
}
```

---

# 86. `None` vs Missing Key

These are different states:

```python
user = {
    "phone": None,
}
```

The key exists.

This user:

```python
user = {}
```

does not contain `"phone"`.

Distinguish them:

```python
if "phone" not in user:
    print("Missing key")
elif user["phone"] is None:
    print("Key exists but has no value")
```

This distinction is important in APIs and partial updates.

---

# 87. Common Mistakes

### Mistake 1: Missing key

```python
user["email"]
```

Use:

```python
user.get("email")
```

when appropriate.

### Mistake 2: Thinking `in` checks values

```python
"Ali" in user
```

checks keys, not values.

Use:

```python
"Ali" in user.values()
```

### Mistake 3: Assuming `copy()` is deep

```python
d.copy()
```

is shallow.

### Mistake 4: Modifying size during iteration

Use a copied list of keys or a comprehension.

### Mistake 5: Overly nested dictionaries

If you repeatedly write:

```python
data["a"]["b"]["c"]["d"]["e"]
```

consider a better data model.

---

# 88. Dictionary Method Complete Reference

| Method | Purpose | Example |
|---|---|---|
| `clear()` | Remove all items | `d.clear()` |
| `copy()` | Shallow copy | `d.copy()` |
| `fromkeys()` | Create from keys | `dict.fromkeys(keys, 0)` |
| `get()` | Safe lookup | `d.get("name")` |
| `items()` | Key-value view | `d.items()` |
| `keys()` | Keys view | `d.keys()` |
| `pop()` | Remove key and return value | `d.pop("age")` |
| `popitem()` | Remove last item | `d.popitem()` |
| `setdefault()` | Get/create default | `d.setdefault("x", 0)` |
| `update()` | Add/update many items | `d.update(other)` |
| `values()` | Values view | `d.values()` |

---

# 89. Built-in Functions and Dictionary Operations

Important built-ins:

| Function | Purpose |
|---|---|
| `len(d)` | Number of keys |
| `list(d)` | Keys as a list |
| `dict(...)` | Create/convert dictionary |
| `sorted(d)` | Sort keys |
| `reversed(d)` | Reverse key iteration |
| `min(d)` | Minimum key |
| `max(d)` | Maximum key |
| `sum(d.values())` | Sum values |
| `any(d.values())` | At least one truthy value |
| `all(d.values())` | All values truthy |
| `enumerate(d)` | Index + keys |
| `zip()` | Combine sequences |

Remember: not every built-in is a dictionary method. These are general Python functions that are frequently useful with dictionaries.

---

# 90. Python's Other Dictionary-Like Tools

## `defaultdict`

Best for automatic default values and grouping.

## `Counter`

Best for counting frequencies.

## `OrderedDict`

Historically important for ordering behavior; normal `dict` preserves insertion order in modern Python. `OrderedDict` can still be useful when its specialized ordering methods are needed.

---

# 91. Practical Project: Student Report

```python
students = {
    101: {
        "name": "Ahmed",
        "grades": {
            "python": 90,
            "django": 85,
            "sql": 95,
        },
        "active": True,
    },
    102: {
        "name": "Ali",
        "grades": {
            "python": 80,
            "django": 75,
            "sql": 88,
        },
        "active": False,
    },
}
```

Average for each student:

```python
averages = {
    student_id:
        sum(student["grades"].values())
        / len(student["grades"])
    for student_id, student in students.items()
}
```

Best course:

```python
best_courses = {
    student_id: max(
        student["grades"],
        key=student["grades"].get,
    )
    for student_id, student in students.items()
}
```

Active students:

```python
active_students = {
    student_id: student
    for student_id, student in students.items()
    if student["active"]
}
```

Best Python student:

```python
best_python_student = max(
    students,
    key=lambda student_id:
        students[student_id]["grades"].get("python", 0)
)

print(students[best_python_student]["name"])
```

---

# 92. Another Real Example: E-commerce Product Index

Input:

```python
products = [
    {
        "id": 101,
        "name": "Chair",
        "price": 2500,
        "stock": 10,
    },
    {
        "id": 102,
        "name": "Desk",
        "price": 5000,
        "stock": 5,
    },
    {
        "id": 103,
        "name": "Lamp",
        "price": 1200,
        "stock": 0,
    },
]
```

Create index:

```python
products_by_id = {
    product["id"]: product
    for product in products
}
```

Find:

```python
product = products_by_id.get(102)

if product:
    print(product["name"])
```

Find out-of-stock items:

```python
out_of_stock = [
    product
    for product in products
    if product["stock"] == 0
]
```

Calculate total inventory value:

```python
inventory_value = sum(
    product["price"] * product["stock"]
    for product in products
)
```

---

# 93. Advanced Challenge: Normalize API Data

Suppose an API returns:

```python
users = [
    {
        "id": 1,
        "profile": {
            "name": "Ahmed",
        },
    },
    {
        "id": 2,
        "profile": {
            "name": "Ali",
        },
    },
]
```

Create:

```python
{
    1: "Ahmed",
    2: "Ali",
}
```

Solution:

```python
user_names = {
    user["id"]: user["profile"]["name"]
    for user in users
}
```

---

# 94. Advanced Challenge: Group Orders and Sum Revenue

```python
orders = [
    {"customer": "Ahmed", "total": 100},
    {"customer": "Ali", "total": 200},
    {"customer": "Ahmed", "total": 150},
]
```

Solution:

```python
revenue_by_customer = {}

for order in orders:
    customer = order["customer"]

    revenue_by_customer[customer] = (
        revenue_by_customer.get(customer, 0)
        + order["total"]
    )
```

Result:

```python
{
    "Ahmed": 250,
    "Ali": 200,
}
```

---

# 95. Teaching Sequence

A strong lesson sequence is:

## Part 1 — Fundamentals

1. What is a dictionary?
2. Key-value concept.
3. Creating dictionaries.
4. Keys and values.
5. Accessing values.
6. Adding data.
7. Updating data.
8. Removing data.
9. `in`.

## Part 2 — Core Methods

10. `get()`
11. `keys()`
12. `values()`
13. `items()`
14. `update()`
15. `pop()`
16. `popitem()`
17. `setdefault()`
18. `clear()`
19. `copy()`
20. `fromkeys()`.

## Part 3 — Loops

21. Keys.
22. Values.
23. Items.
24. Counting.
25. Grouping.

## Part 4 — Comprehensions

26. Dictionary comprehension.
27. Filtering.
28. Transformation.
29. Nested structures.

## Part 5 — Real World

30. JSON.
31. API responses.
32. Product inventory.
33. Student systems.
34. Configuration.
35. Lookup tables.

## Part 6 — Advanced

36. Shallow vs deep copy.
37. Hashability.
38. `|` and `|=`.
39. `defaultdict`.
40. `Counter`.
41. Type hints.
42. `TypedDict`.
43. Pattern matching.
44. Recursive processing.

---

# 96. Exercises

## Beginner

### Exercise 1

Create:

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "city": "Cairo",
}
```

Print all values.

### Exercise 2

Add `"grade": 90`, then update it to `95`.

### Exercise 3

Remove `"city"` using `pop()`.

### Exercise 4

Check for `"email"` without causing `KeyError`.

---

## Intermediate

### Exercise 5 — Counting

```python
words = [
    "python",
    "django",
    "python",
    "flask",
    "django",
    "python",
]
```

Create frequency counts.

### Exercise 6 — Filtering

```python
scores = {
    "Ahmed": 90,
    "Ali": 70,
    "Mona": 95,
    "Omar": 60,
}
```

Keep only scores >= 80.

### Exercise 7 — Highest Score

Find the student with the highest score.

---

## Advanced

### Exercise 8 — Grouping

```python
employees = [
    {"name": "Ahmed", "department": "IT"},
    {"name": "Ali", "department": "HR"},
    {"name": "Mona", "department": "IT"},
    {"name": "Omar", "department": "HR"},
]
```

Create:

```python
{
    "IT": ["Ahmed", "Mona"],
    "HR": ["Ali", "Omar"],
}
```

### Exercise 9 — Product Index

Create a dictionary indexed by product ID.

### Exercise 10 — Student Report

Given each student's grade list, calculate:

- average
- highest grade
- lowest grade
- pass/fail

---

# 97. Interview Questions

### Q1. What is a dictionary?

A mutable mapping of unique keys to values.

### Q2. Can a list be a dictionary key?

No. Lists are unhashable.

### Q3. What is the difference between `d["key"]` and `d.get("key")`?

`d["key"]` raises `KeyError` if missing. `get()` returns `None` or a supplied default.

### Q4. What does `items()` return?

A dynamic view of key-value pairs.

### Q5. What does `setdefault()` do?

Reads an existing value or creates the key with a default when missing.

### Q6. What is a shallow copy?

A new outer dictionary that can still share nested objects.

### Q7. What is average dictionary lookup complexity?

Approximately O(1).

### Q8. What happens with duplicate keys?

The later value replaces the earlier one.

### Q9. Difference between `a = b` and `a = b.copy()`?

The first shares the same object. The second creates a shallow copy.

### Q10. How can dictionaries be merged?

```python
a | b
```

or:

```python
a.update(b)
```

or:

```python
{**a, **b}
```

---

# 98. Final Mental Model

Think about a dictionary as:

```text
Dictionary
│
├── key
│   └── identifies data
│
├── value
│   └── stores data
│
├── mutable
│
├── unique keys
│
├── hashable keys
│
├── fast average lookup
│
├── insertion order preserved
│
├── nested data
│
├── comprehensions
│
└── powerful lookup/grouping patterns
```

The core model is always:

```python
dictionary[key] = value
```

Everything else builds on this.

---

# 99. Complete Cheat Sheet

```python
# Create
user = {
    "name": "Ali",
    "age": 20,
}

# Read
user["name"]

# Safe read
user.get("email")
user.get("email", "Not provided")

# Add / update
user["city"] = "Cairo"
user["age"] = 21

# Multiple update
user.update({
    "job": "Developer",
    "active": True,
})

# Check key
"name" in user

# Keys / values / items
user.keys()
user.values()
user.items()

# Delete
del user["city"]

# Pop
user.pop("age")

# Last item
user.popitem()

# Clear
user.clear()

# Copy
new_user = user.copy()

# Default
user.setdefault("country", "Egypt")

# Build from keys
dict.fromkeys(["a", "b"], 0)

# Dictionary comprehension
squares = {
    x: x ** 2
    for x in range(1, 6)
}

# Filtering
filtered = {
    key: value
    for key, value in data.items()
    if value > 10
}

# Merge
result = a | b

# In-place merge
a |= b

# Iterate
for key, value in user.items():
    print(key, value)

# Sum
total = sum(scores.values())

# Best value
best = max(scores, key=scores.get)

# Create from two sequences
data = dict(zip(keys, values))
```

---

# 100. Conclusion

Python dictionaries are one of the most important data structures in Python.

Students should master:

```text
key-value
access
add
update
delete
get
in
keys
values
items
loops
nested dictionaries
dictionary comprehension
counting
grouping
sorting
merging
copying
hashability
JSON
API data
```

Then move into:

```text
defaultdict
Counter
TypedDict
deep merge
recursive processing
dispatch tables
indexing
pattern matching
advanced typing
```

The central idea is simple:

```python
dictionary[key] = value
```

Once that idea is understood deeply, dictionaries become one of the most powerful and flexible tools in Python.
