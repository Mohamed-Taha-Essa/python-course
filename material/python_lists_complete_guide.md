# Python Lists — Complete Guide from Beginner to Advanced

> A practical, teaching-oriented guide to Python `list` from the first example to advanced patterns, performance considerations, and common pitfalls.

---

## Table of Contents

1. [What is a List?](#1-what-is-a-list)
2. [Creating Lists](#2-creating-lists)
3. [Indexing](#3-indexing)
4. [Negative Indexing](#4-negative-indexing)
5. [Changing List Items](#5-changing-list-items)
6. [List Length](#6-list-length)
7. [Adding Items](#7-adding-items)
8. [Removing Items](#8-removing-items)
9. [Searching and Counting](#9-searching-and-counting)
10. [Sorting and Reversing](#10-sorting-and-reversing)
11. [Copying Lists](#11-copying-lists)
12. [Joining Lists](#12-joining-lists)
13. [List Slicing](#13-list-slicing)
14. [Extended Slicing](#14-extended-slicing)
15. [Iterating Over Lists](#15-iterating-over-lists)
16. [List Comprehensions](#16-list-comprehensions)
17. [Nested Lists](#17-nested-lists)
18. [The `list()` Constructor](#18-the-list-constructor)
19. [All Important List Methods](#19-all-important-list-methods)
20. [Built-in Functions Commonly Used With Lists](#20-built-in-functions-commonly-used-with-lists)
21. [`enumerate()`](#21-enumerate)
22. [`zip()`](#22-zip)
23. [`map()` and `filter()`](#23-map-and-filter)
24. [`all()` and `any()`](#24-all-and-any)
25. [`sorted()` vs `.sort()`](#25-sorted-vs-sort)
26. [Mutability and References](#26-mutability-and-references)
27. [Shallow Copy vs Deep Copy](#27-shallow-copy-vs-deep-copy)
28. [Common List Pitfalls](#28-common-list-pitfalls)
29. [Performance and Big-O](#29-performance-and-big-o)
30. [Advanced Patterns](#30-advanced-patterns)
31. [Lists vs Tuples vs Sets](#31-lists-vs-tuples-vs-sets)
32. [Practice Exercises](#32-practice-exercises)
33. [Quick Reference Cheat Sheet](#33-quick-reference-cheat-sheet)

---

# 1. What is a List?

A Python `list` is an **ordered, mutable collection** that can store zero or more values.

```python
numbers = [10, 20, 30, 40]
```

The important characteristics are:

- **Ordered**: items keep a defined position.
- **Mutable**: items can be changed after the list is created.
- **Indexed**: items can be accessed using numeric indexes.
- **Allows duplicates**: the same value can appear more than once.
- **Can contain mixed types**: a list can hold integers, strings, objects, and even other lists.

Example:

```python
mixed = [10, "Python", 3.14, True, None]
```

A list can also contain another list:

```python
nested = [1, 2, [3, 4, 5]]
```

---

# 2. Creating Lists

## 2.1 Empty list

```python
items = []
```

## 2.2 List with values

```python
names = ["Ali", "Mona", "Omar"]
```

## 2.3 Mixed data types

```python
student = [101, "Mohamed", 22, 3.8, True]
```

## 2.4 Using `list()`

```python
letters = list("Python")
print(letters)
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

The `list()` constructor converts an iterable into a list.

```python
numbers = list(range(1, 6))
print(numbers)
# [1, 2, 3, 4, 5]
```

You can convert tuples, sets, strings, generators, and other iterables:

```python
list((1, 2, 3))
list({4, 5, 6})
list("abc")
```

---

# 3. Indexing

Every list item has an index starting from `0`.

```python
fruits = ["apple", "banana", "orange", "mango"]
```

| Item | Index |
|---|---:|
| apple | 0 |
| banana | 1 |
| orange | 2 |
| mango | 3 |

Access values like this:

```python
print(fruits[0])
print(fruits[2])
```

Output:

```text
apple
orange
```

## IndexError

An invalid index raises `IndexError`:

```python
fruits[10]
```

Possible error:

```text
IndexError: list index out of range
```

---

# 4. Negative Indexing

Negative indexes count from the end.

```python
fruits = ["apple", "banana", "orange", "mango"]
```

| Item | Negative Index |
|---|---:|
| apple | -4 |
| banana | -3 |
| orange | -2 |
| mango | -1 |

Examples:

```python
print(fruits[-1])  # mango
print(fruits[-2])  # orange
```

Negative indexing is useful when you need the last few elements without calculating the list length manually.

---

# 5. Changing List Items

Because lists are mutable, an item can be replaced by assigning to its index.

```python
numbers = [10, 20, 30]
numbers[1] = 200

print(numbers)
```

Output:

```text
[10, 200, 30]
```

You can also replace a range of values with slicing:

```python
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [20, 30, 40]
print(numbers)
```

Output:

```text
[1, 20, 30, 40, 5]
```

The replacement slice does **not** have to contain the same number of values:

```python
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [99]
print(numbers)
```

Output:

```text
[1, 99, 5]
```

---

# 6. List Length

Use the built-in `len()` function:

```python
numbers = [10, 20, 30, 40]
print(len(numbers))
```

Output:

```text
4
```

Remember:

- `len(list)` returns the number of elements.
- The last positive index is `len(list) - 1`.

Example:

```python
last_index = len(numbers) - 1
print(numbers[last_index])
```

---

# 7. Adding Items

Python lists provide three main methods for adding items:

- `append()` — add one item at the end.
- `extend()` — add multiple items from an iterable.
- `insert()` — add one item at a specific position.

## 7.1 `append()`

```python
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
# [1, 2, 3, 4]
```

### Important behavior

`append()` adds the argument as **one single element**.

```python
numbers = [1, 2, 3]
numbers.append([4, 5])

print(numbers)
# [1, 2, 3, [4, 5]]
```

This creates a nested list.

---

## 7.2 `extend()`

`extend()` adds every element from an iterable.

```python
numbers = [1, 2, 3]
numbers.extend([4, 5])

print(numbers)
# [1, 2, 3, 4, 5]
```

It can use any iterable:

```python
letters = ["a", "b"]
letters.extend("cd")
print(letters)
# ['a', 'b', 'c', 'd']
```

### `append()` vs `extend()`

```python
x = [1, 2]
x.append([3, 4])
print(x)
# [1, 2, [3, 4]]

x = [1, 2]
x.extend([3, 4])
print(x)
# [1, 2, 3, 4]
```

---

## 7.3 `insert()`

Syntax:

```python
list.insert(index, value)
```

Example:

```python
numbers = [10, 20, 40]
numbers.insert(2, 30)
print(numbers)
# [10, 20, 30, 40]
```

At the beginning:

```python
numbers.insert(0, 5)
```

A negative index can also be used:

```python
numbers.insert(-1, 999)
```

For very large lists, frequent insertion near the beginning is expensive because other elements must be shifted.

---

# 8. Removing Items

The main removal operations are:

- `remove()` — remove by value.
- `pop()` — remove by index and return the removed item.
- `clear()` — remove everything.
- `del` — delete an item, slice, or variable binding.

## 8.1 `remove()`

```python
names = ["Ali", "Omar", "Ali", "Mona"]
names.remove("Ali")

print(names)
# ['Omar', 'Ali', 'Mona']
```

It removes the **first matching value only**.

If the value does not exist:

```python
names.remove("Ahmed")
```

This raises:

```text
ValueError: list.remove(x): x not in list
```

Safe pattern:

```python
if "Ahmed" in names:
    names.remove("Ahmed")
```

---

## 8.2 `pop()`

Remove and return an item.

```python
numbers = [10, 20, 30]
removed = numbers.pop()

print(removed)
# 30
print(numbers)
# [10, 20]
```

Remove a specific index:

```python
numbers = [10, 20, 30]
removed = numbers.pop(1)

print(removed)
# 20
print(numbers)
# [10, 30]
```

Using an invalid index raises `IndexError`.

### Why `pop()` is useful

It can be used to implement stack-like behavior:

```python
stack = []
stack.append("first")
stack.append("second")
stack.append("third")

item = stack.pop()
print(item)
# third
```

A list is excellent as a stack because appending and popping at the end are efficient.

---

## 8.3 `clear()`

Remove every item while keeping the list object itself.

```python
numbers = [1, 2, 3]
numbers.clear()

print(numbers)
# []
```

Compare:

```python
numbers = [1, 2, 3]
numbers = []
```

The second example rebinds the variable to a different list object. `clear()` mutates the original object.

---

## 8.4 `del`

`del` is a Python statement, not a list method.

Delete one item:

```python
numbers = [10, 20, 30]
del numbers[1]
print(numbers)
# [10, 30]
```

Delete a slice:

```python
numbers = [1, 2, 3, 4, 5]
del numbers[1:4]
print(numbers)
# [1, 5]
```

Delete everything:

```python
del numbers[:]
```

Delete the variable binding itself:

```python
del numbers
```

After that, using `numbers` causes `NameError`.

---

# 9. Searching and Counting

## 9.1 `in`

Use the membership operator:

```python
names = ["Ali", "Omar", "Mona"]

print("Omar" in names)
# True

print("Ahmed" in names)
# False
```

For absence:

```python
print("Ahmed" not in names)
# True
```

## 9.2 `index()`

Returns the first index of a matching value.

```python
letters = ["a", "b", "c", "b"]
print(letters.index("b"))
# 1
```

You can define a start and stop position:

```python
letters.index("b", 2)
# 3
```

Formally:

```python
list.index(value, start=0, stop=len(list))
```

If not found, `ValueError` is raised.

---

## 9.3 `count()`

Count how many times a value occurs:

```python
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))
# 3
```

For a large list, repeated `count()` calls may be inefficient. If you need frequencies of many values, consider `collections.Counter`.

```python
from collections import Counter

numbers = [1, 2, 2, 3, 2]
counts = Counter(numbers)
print(counts)
# Counter({2: 3, 1: 1, 3: 1})
```

---

# 10. Sorting and Reversing

## 10.1 `sort()`

`sort()` sorts the list **in place**.

```python
numbers = [5, 1, 4, 2, 3]
numbers.sort()
print(numbers)
# [1, 2, 3, 4, 5]
```

Descending order:

```python
numbers.sort(reverse=True)
```

### Sorting strings

```python
names = ["Omar", "Ali", "Mona"]
names.sort()
print(names)
```

### Sorting by a key

```python
students = [
    {"name": "Ali", "grade": 90},
    {"name": "Omar", "grade": 75},
    {"name": "Mona", "grade": 95},
]

students.sort(key=lambda student: student["grade"])
```

Descending by grade:

```python
students.sort(key=lambda student: student["grade"], reverse=True)
```

### `key` does not change what is stored

The key function tells Python what value to use for comparison.

Example: case-insensitive sorting:

```python
names = ["ali", "Mona", "OMAR", "ahmed"]
names.sort(key=str.lower)
```

---

## 10.2 `reverse()`

Reverse the list **in place**.

```python
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)
# [4, 3, 2, 1]
```

Important: `reverse()` does **not** sort.

```python
numbers = [3, 1, 4, 2]
numbers.reverse()
# [2, 4, 1, 3]
```

It simply reverses the existing order.

---

# 11. Copying Lists

This is one of the most important list concepts for beginners.

## 11.1 Assignment does not create a new list

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
# [1, 2, 3, 4]
```

Both variables refer to the same list object.

You can verify with `is`:

```python
print(a is b)
# True
```

---

## 11.2 Shallow copies

Create a new outer list using:

```python
b = a.copy()
```

or:

```python
b = a[:]
```

or:

```python
b = list(a)
```

Example:

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
# [1, 2, 3]

print(b)
# [1, 2, 3, 4]
```

---

# 12. Joining Lists

## 12.1 `+`

Create a new list:

```python
a = [1, 2]
b = [3, 4]

result = a + b
print(result)
# [1, 2, 3, 4]
```

`a` and `b` remain unchanged.

## 12.2 `extend()`

Modify an existing list:

```python
a = [1, 2]
a.extend([3, 4])
```

## 12.3 Repetition with `*`

```python
zeros = [0] * 5
print(zeros)
# [0, 0, 0, 0, 0]
```

### Important nested-list warning

This is dangerous:

```python
matrix = [[0] * 3] * 3
```

All rows refer to the same inner list.

```python
matrix[0][0] = 1
print(matrix)
```

Result:

```text
[[1, 0, 0], [1, 0, 0], [1, 0, 0]]
```

Correct approach:

```python
matrix = [[0] * 3 for _ in range(3)]
```

Now each row is a separate list.

---

# 13. List Slicing

Slicing lets you extract a portion of a list.

Syntax:

```python
list[start:stop]
```

`start` is inclusive and `stop` is exclusive.

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])
# [1, 2, 3]
```

The indexes included are `1`, `2`, `3`.

## Start omitted

```python
numbers[:3]
# [0, 1, 2]
```

## Stop omitted

```python
numbers[3:]
# [3, 4, 5]
```

## Both omitted

```python
numbers[:]
```

This is a shallow copy of the outer list.

---

# 14. Extended Slicing

Syntax:

```python
list[start:stop:step]
```

## Every second item

```python
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[::2])
# [0, 2, 4, 6]
```

## Reverse a list

```python
print(numbers[::-1])
# [6, 5, 4, 3, 2, 1, 0]
```

Unlike `reverse()`, slicing creates a new list.

## Replace using slices

```python
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30, 40]
print(numbers)
# [1, 20, 30, 40, 4, 5]
```

With an extended slice (`step != 1`), the replacement must have the same number of elements:

```python
numbers[::2] = [100, 200, 300]
```

The sizes must match.

---

# 15. Iterating Over Lists

## Basic loop

```python
names = ["Ali", "Mona", "Omar"]

for name in names:
    print(name)
```

## Index and value

```python
for index in range(len(names)):
    print(index, names[index])
```

A more Pythonic solution uses `enumerate()`:

```python
for index, name in enumerate(names):
    print(index, name)
```

Custom starting index:

```python
for index, name in enumerate(names, start=1):
    print(index, name)
```

---

# 16. List Comprehensions

A list comprehension is a compact way to create a new list.

Basic form:

```python
[expression for item in iterable]
```

Example:

```python
squares = [x ** 2 for x in range(6)]
print(squares)
# [0, 1, 4, 9, 16, 25]
```

## With condition

```python
even = [x for x in range(10) if x % 2 == 0]
print(even)
# [0, 2, 4, 6, 8]
```

## Transformation

```python
names = ["ali", "mona", "omar"]
upper_names = [name.upper() for name in names]
```

## Conditional expression

```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
```

## Nested comprehension

```python
pairs = [(x, y) for x in range(3) for y in range(2)]
```

Nested comprehensions are powerful, but readability matters. A normal loop can be better when the logic becomes complicated.

---

# 17. Nested Lists

A list can contain other lists.

```python
students = [
    ["Ali", 90],
    ["Mona", 95],
    ["Omar", 80],
]
```

Access nested data:

```python
print(students[0][0])
# Ali

print(students[1][1])
# 95
```

A more descriptive structure may use dictionaries:

```python
students = [
    {"name": "Ali", "grade": 90},
    {"name": "Mona", "grade": 95},
]
```

Choose the structure based on the problem instead of using lists everywhere.

---

# 18. The `list()` Constructor

`list()` accepts an iterable and creates a list.

```python
list("hello")
# ['h', 'e', 'l', 'l', 'o']
```

```python
list(range(5))
# [0, 1, 2, 3, 4]
```

```python
list((1, 2, 3))
# [1, 2, 3]
```

A generator can be materialized:

```python
generator = (x * 2 for x in range(5))
result = list(generator)
print(result)
# [0, 2, 4, 6, 8]
```

Remember that converting a large or infinite iterable into a list may use a lot of memory or never finish.

---

# 19. All Important List Methods

Python's built-in `list` type provides these methods:

| Method | Purpose | Returns |
|---|---|---|
| `append(x)` | Add one item at end | `None` |
| `clear()` | Remove all items | `None` |
| `copy()` | Shallow copy | New list |
| `count(x)` | Count occurrences | `int` |
| `extend(iterable)` | Add items from iterable | `None` |
| `index(x[, start[, stop]])` | Find first matching index | `int` |
| `insert(i, x)` | Insert item at index | `None` |
| `pop([i])` | Remove and return item | Item |
| `remove(x)` | Remove first matching value | `None` |
| `reverse()` | Reverse in place | `None` |
| `sort(...)` | Sort in place | `None` |

These are the list-specific methods you should know thoroughly.

## Critical pattern: mutation methods often return `None`

Do not write:

```python
numbers = [3, 1, 2]
numbers = numbers.sort()
```

After this, `numbers` becomes `None`.

Correct:

```python
numbers = [3, 1, 2]
numbers.sort()
```

Likewise:

```python
numbers.append(4)    # mutate
numbers.extend([5])  # mutate
numbers.reverse()    # mutate
numbers.sort()       # mutate
```

---

# 20. Built-in Functions Commonly Used With Lists

The following are Python built-in functions that work especially well with lists.

## `len()`

```python
numbers = [10, 20, 30]
print(len(numbers))
# 3
```

## `min()`

```python
numbers = [7, 2, 9, 1]
print(min(numbers))
# 1
```

## `max()`

```python
print(max(numbers))
# 9
```

## `sum()`

```python
print(sum(numbers))
# 19
```

`sum()` is intended for numeric values and compatible numeric types.

You can provide a starting value:

```python
numbers = [1, 2, 3]
print(sum(numbers, 100))
# 106
```

## `sorted()`

Returns a **new list** instead of modifying the original:

```python
numbers = [3, 1, 2]
result = sorted(numbers)

print(result)
# [1, 2, 3]

print(numbers)
# [3, 1, 2]
```

Descending:

```python
sorted(numbers, reverse=True)
```

With `key`:

```python
names = ["Mohamed", "Ali", "ahmed"]
result = sorted(names, key=str.lower)
```

## `reversed()`

Returns an iterator, not a new list immediately:

```python
numbers = [1, 2, 3]
r = reversed(numbers)

print(list(r))
# [3, 2, 1]
```

Compare:

```python
numbers.reverse()     # changes the list
reversed(numbers)     # creates an iterator
numbers[::-1]         # creates a new list
```

## `all()`

Returns `True` if all elements are truthy.

```python
values = [True, 1, "hello"]
print(all(values))
# True
```

```python
values = [True, 1, 0]
print(all(values))
# False
```

## `any()`

Returns `True` if at least one element is truthy.

```python
values = [0, False, 10]
print(any(values))
# True
```

## `enumerate()`

Produces index-value pairs:

```python
names = ["Ali", "Mona", "Omar"]

for index, name in enumerate(names):
    print(index, name)
```

## `zip()`

Combines elements from multiple iterables:

```python
names = ["Ali", "Mona", "Omar"]
grades = [90, 95, 80]

for name, grade in zip(names, grades):
    print(name, grade)
```

## `map()`

Applies a function to every item and returns an iterator.

```python
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))
# [2, 4, 6, 8]
```

For many simple transformations, a list comprehension is often more readable:

```python
result = [x * 2 for x in numbers]
```

## `filter()`

Keeps items for which a condition is true.

```python
numbers = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))
# [2, 4]
```

Equivalent comprehension:

```python
result = [x for x in numbers if x % 2 == 0]
```

## `type()`

```python
numbers = [1, 2, 3]
print(type(numbers))
# <class 'list'>
```

## `isinstance()`

Prefer this for type checking:

```python
numbers = [1, 2, 3]
print(isinstance(numbers, list))
# True
```

## `id()`

Useful for teaching references and object identity:

```python
a = [1, 2]
b = a

print(id(a) == id(b))
# True
```

## `iter()` and `next()`

Lists are iterable.

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))
# 10
print(next(iterator))
# 20
```

When there are no more items, `next()` raises `StopIteration` unless a default is supplied:

```python
print(next(iterator, None))
```

## `repr()` and `str()`

```python
numbers = [1, 2, 3]
print(str(numbers))
print(repr(numbers))
```

For a list, the representations are commonly visually similar, but `repr()` is intended as a developer-oriented representation.

---

# 21. `enumerate()`

`enumerate()` is one of the most useful built-ins for lists.

Bad/less Pythonic approach:

```python
names = ["Ali", "Mona", "Omar"]

for i in range(len(names)):
    print(i, names[i])
```

Better:

```python
for i, name in enumerate(names):
    print(i, name)
```

Start counting at `1`:

```python
for number, name in enumerate(names, start=1):
    print(number, name)
```

You can materialize the result:

```python
pairs = list(enumerate(names))
```

Output:

```text
[(0, 'Ali'), (1, 'Mona'), (2, 'Omar')]
```

---

# 22. `zip()`

`zip()` allows parallel iteration.

```python
names = ["Ali", "Mona", "Omar"]
ages = [20, 21, 19]

for name, age in zip(names, ages):
    print(name, age)
```

You can convert it into a list:

```python
pairs = list(zip(names, ages))
```

Result:

```text
[('Ali', 20), ('Mona', 21), ('Omar', 19)]
```

## Different lengths

By default, `zip()` stops when the shortest iterable ends.

```python
print(list(zip([1, 2, 3], ["a", "b"])))
# [(1, 'a'), (2, 'b')]
```

For stricter behavior in modern Python, `zip(..., strict=True)` can be used when the inputs are expected to have the same length:

```python
zip(names, ages, strict=True)
```

If lengths differ, a `ValueError` is raised during iteration.

---

# 23. `map()` and `filter()`

## `map()` with a normal function

```python
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
result = list(map(square, numbers))
print(result)
# [1, 4, 9, 16]
```

## `map()` with multiple iterables

```python
a = [1, 2, 3]
b = [10, 20, 30]

result = list(map(lambda x, y: x + y, a, b))
print(result)
# [11, 22, 33]
```

## `filter()`

```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4]
result = list(filter(is_even, numbers))
```

List comprehensions are usually preferred when readability is better:

```python
result = [x for x in numbers if is_even(x)]
```

---

# 24. `all()` and `any()`

These are extremely useful for validation.

## `all()` example

Check that every grade is valid:

```python
grades = [90, 80, 75, 88]

valid = all(0 <= grade <= 100 for grade in grades)
print(valid)
# True
```

## `any()` example

Check whether at least one grade is perfect:

```python
has_perfect = any(grade == 100 for grade in grades)
```

Notice that we can pass a generator expression instead of building an unnecessary list.

This can save memory and can stop early when the result is already known.

---

# 25. `sorted()` vs `.sort()`

This distinction is essential.

## `.sort()`

- List method.
- Modifies the original list.
- Returns `None`.

```python
numbers = [3, 1, 2]
numbers.sort()
```

## `sorted()`

- Built-in function.
- Returns a new sorted list.
- Works with many iterables, not only lists.

```python
numbers = [3, 1, 2]
result = sorted(numbers)
```

Example with a tuple:

```python
values = (3, 1, 2)
result = sorted(values)
print(type(result))
# <class 'list'>
```

---

# 26. Mutability and References

This is a core Python concept.

```python
a = [1, 2, 3]
b = a
```

The variables do not contain independent copies. They refer to the same list object.

```python
b.append(4)
print(a)
# [1, 2, 3, 4]
```

## Identity vs equality

`==` compares values:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
# True
```

`is` compares object identity:

```python
print(a is b)
# False
```

Same object:

```python
c = a
print(a is c)
# True
```

### Rule

Use:

- `==` when asking: "Do these values compare equal?"
- `is` when asking: "Are these the exact same object?"

Do not normally use `is` for ordinary value comparisons such as strings or integers.

---

# 27. Shallow Copy vs Deep Copy

Suppose a list contains nested mutable objects:

```python
original = [[1, 2], [3, 4]]
copy1 = original.copy()
```

The outer list is different:

```python
print(original is copy1)
# False
```

But the inner lists are shared:

```python
print(original[0] is copy1[0])
# True
```

Therefore:

```python
copy1[0].append(99)
print(original)
# [[1, 2, 99], [3, 4]]
```

## Deep copy

Use `copy.deepcopy()` when you need recursive copying of nested objects:

```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0].append(99)

print(original)
# [[1, 2], [3, 4]]
```

Use deep copying carefully: it can be expensive and is not always necessary.

---

# 28. Common List Pitfalls

## Pitfall 1: `sort()` returns `None`

Wrong:

```python
numbers = [3, 1, 2]
result = numbers.sort()
print(result)
# None
```

Correct:

```python
numbers.sort()
```

Or:

```python
result = sorted(numbers)
```

---

## Pitfall 2: `append()` vs `extend()`

```python
items = [1, 2]
items.append([3, 4])
# [1, 2, [3, 4]]
```

Use `extend()` when you want individual values:

```python
items = [1, 2]
items.extend([3, 4])
# [1, 2, 3, 4]
```

---

## Pitfall 3: Removing while iterating

Dangerous pattern:

```python
numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)
```

Removing elements changes indexes while the loop is running, which can cause skipped elements or confusing behavior.

Better:

```python
numbers = [number for number in numbers if number % 2 != 0]
```

Or iterate over a copy when mutation is specifically required:

```python
for number in numbers[:]:
    if number % 2 == 0:
        numbers.remove(number)
```

---

## Pitfall 4: Using `[*] * n` with nested mutable values

Dangerous:

```python
matrix = [[0] * 3] * 3
```

Correct:

```python
matrix = [[0] * 3 for _ in range(3)]
```

---

## Pitfall 5: Confusing a list with a single element

```python
numbers = [1, 2, 3]
```

The whole list is one object containing three elements.

When passing a list to a function:

```python
def process(items):
    print(items)

process([1, 2, 3])
```

Be clear about whether the function expects one object or multiple arguments.

---

# 29. Performance and Big-O

For teaching and practical development, understanding the rough cost of operations is valuable.

| Operation | Typical complexity |
|---|---:|
| `a[i]` | O(1) |
| `a[i] = x` | O(1) |
| `append(x)` | Amortized O(1) |
| `pop()` from end | O(1) |
| `insert(0, x)` | O(n) |
| `pop(0)` | O(n) |
| `remove(x)` | O(n) |
| `x in a` | O(n) |
| `index(x)` | O(n) |
| `count(x)` | O(n) |
| `sort()` | O(n log n) typical |

## Why are front operations expensive?

Lists are dynamic arrays. Inserting or removing near the beginning usually requires shifting many existing elements.

For a queue, repeatedly doing this:

```python
queue.pop(0)
```

is usually a poor design for large workloads.

Use `collections.deque`:

```python
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()
```

`deque` is designed for efficient operations at both ends.

---

# 30. Advanced Patterns

## 30.1 Flattening a 2D list

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

flat = [value for row in matrix for value in row]
print(flat)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Equivalent loops:

```python
flat = []
for row in matrix:
    for value in row:
        flat.append(value)
```

---

## 30.2 Deduplicating while preserving order

Using `dict` keys:

```python
numbers = [3, 1, 3, 2, 1, 4]
unique = list(dict.fromkeys(numbers))
print(unique)
# [3, 1, 2, 4]
```

This is a useful technique when values are hashable.

Do not automatically replace lists with sets: sets are unordered collections in terms of sequence semantics, and they have different use cases.

---

## 30.3 Sorting objects using `key`

```python
users = [
    {"name": "Ali", "age": 25},
    {"name": "Mona", "age": 20},
    {"name": "Omar", "age": 30},
]

users.sort(key=lambda user: user["age"])
```

More maintainable style:

```python
from operator import itemgetter

users.sort(key=itemgetter("age"))
```

---

## 30.4 Multiple sorting criteria

```python
students = [
    {"name": "Ali", "grade": 90},
    {"name": "Mona", "grade": 90},
    {"name": "Omar", "grade": 85},
]

students.sort(key=lambda student: (student["grade"], student["name"]))
```

Python's sort is stable, which allows advanced multi-pass sorting strategies.

---

## 30.5 Transpose a matrix with `zip()`

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

transposed = [list(column) for column in zip(*matrix)]
print(transposed)
# [[1, 4], [2, 5], [3, 6]]
```

Here, `*matrix` unpacks the rows as separate arguments to `zip()`.

---

## 30.6 Partitioning with a comprehension

```python
numbers = [1, 2, 3, 4, 5, 6]

evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]
```

For complex partitioning logic, consider a normal loop or utilities from the standard library.

---

## 30.7 Use generator expressions when a list is unnecessary

Suppose you only need the sum:

```python
numbers = range(1_000_000)
total = sum(x * x for x in numbers)
```

You do not need:

```python
total = sum([x * x for x in numbers])
```

The generator version avoids creating an extra large list in memory.

---

## 30.8 Starred unpacking

```python
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
# 1
print(middle)
# [2, 3, 4]
print(last)
# 5
```

Another example:

```python
first, second, *rest = numbers
```

`rest` becomes a list.

---

## 30.9 Function arguments and lists

A list can be passed into a function:

```python
def total(numbers):
    return sum(numbers)

print(total([10, 20, 30]))
# 60
```

Unpacking a list into separate positional arguments uses `*`:

```python
numbers = [3, 7, 2]
print(max(*numbers))
```

This is conceptually different from passing the list itself:

```python
max(numbers)
```

---

# 31. Lists vs Tuples vs Sets

| Feature | List | Tuple | Set |
|---|---|---|---|
| Ordered sequence | Yes | Yes | Set semantics are unordered |
| Mutable | Yes | No | Yes |
| Duplicate values | Yes | Yes | No |
| Indexing | Yes | Yes | No |
| Typical use | Changeable collection | Fixed record/sequence | Membership & uniqueness |

Example:

```python
names = ["Ali", "Mona", "Ali"]
coordinates = (30.0, 31.2)
unique_numbers = {1, 2, 3}
```

Choose the data structure according to the operation you need.

---

# 32. Practice Exercises

## Beginner

### Exercise 1
Create a list containing five favorite foods and print the first and last items.

### Exercise 2
Create a list of numbers from 1 to 10 and print only the even numbers.

### Exercise 3
Add a new value to the end of a list using `append()`.

### Exercise 4
Insert a value at index `2`.

### Exercise 5
Remove one value using `remove()` and another using `pop()`.

---

## Intermediate

### Exercise 6
Given:

```python
numbers = [4, 1, 7, 3, 9, 2]
```

Find:

- smallest value
- largest value
- sum
- number of elements
- sorted version

Use built-in functions where appropriate.

### Exercise 7
Count how many times `2` occurs:

```python
numbers = [2, 4, 2, 7, 2, 9, 1]
```

### Exercise 8
Create a new list containing the squares of numbers from `1` to `10` using a list comprehension.

### Exercise 9
Remove all negative values from:

```python
numbers = [4, -1, 7, -3, 2, -8]
```

Do not remove items directly from the list while iterating over it.

---

## Advanced

### Exercise 10
Sort these dictionaries by grade, highest first:

```python
students = [
    {"name": "Ali", "grade": 82},
    {"name": "Mona", "grade": 96},
    {"name": "Omar", "grade": 88},
]
```

### Exercise 11
Flatten:

```python
matrix = [[1, 2], [3, 4], [5, 6]]
```

### Exercise 12
Transpose:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
```

### Exercise 13
Remove duplicate values while preserving the original order:

```python
values = [3, 5, 3, 2, 5, 1, 2]
```

### Exercise 14
Use `all()` to determine whether every number in a list is positive.

### Exercise 15
Use `any()` to determine whether a list contains at least one negative number.

---

# 33. Quick Reference Cheat Sheet

## Create

```python
items = []
items = [1, 2, 3]
items = list(range(5))
```

## Access

```python
items[0]
items[-1]
items[1:4]
items[::2]
items[::-1]
```

## Modify

```python
items[0] = 99
items[1:3] = [7, 8]
```

## Add

```python
items.append(x)
items.extend(iterable)
items.insert(index, x)
```

## Remove

```python
items.remove(x)
items.pop()
items.pop(index)
items.clear()
del items[index]
del items[start:stop]
```

## Search

```python
x in items
x not in items
items.index(x)
items.count(x)
```

## Order

```python
items.sort()
items.sort(reverse=True)
items.sort(key=func)
items.reverse()
sorted(items)
reversed(items)
```

## Copy

```python
items.copy()
items[:]
list(items)
```

## Useful built-ins

```python
len(items)
min(items)
max(items)
sum(items)
all(items)
any(items)
enumerate(items)
zip(items, other)
map(func, items)
filter(func, items)
list(iterable)
```

---

# Final Mental Model

When teaching or learning Python lists, remember these five layers:

## Layer 1 — Access

```python
items[index]
items[start:stop]
```

## Layer 2 — Mutation

```python
append()
extend()
insert()
remove()
pop()
clear()
sort()
reverse()
```

## Layer 3 — Querying

```python
in
index()
count()
len()
min()
max()
sum()
```

## Layer 4 — Transforming

```python
list_comprehension
map()
filter()
sorted()
```

## Layer 5 — Advanced Pythonic Patterns

```python
enumerate()
zip()
all()
any()
star_unpacking
nested_comprehensions
shallow_copy
copy.deepcopy()
```

The most important concepts to master are not just memorizing methods. A strong Python developer should understand **mutability, references, slicing, iteration, comprehensions, sorting with `key`, copying, and the performance cost of operations**.

---

# Instructor Notes: Recommended Teaching Sequence

For a classroom session, a strong sequence is:

1. What a list is and why we use it.
2. Creating lists.
3. Indexing and negative indexing.
4. Updating elements.
5. `len()`.
6. `append()`, `insert()`, `extend()`.
7. `remove()`, `pop()`, `clear()`, `del`.
8. `in`, `index()`, `count()`.
9. `sort()`, `reverse()`, `sorted()`, `reversed()`.
10. Slicing.
11. Loops and `enumerate()`.
12. List comprehensions.
13. Nested lists.
14. References and copying.
15. Built-ins: `sum()`, `min()`, `max()`, `all()`, `any()`, `zip()`, `map()`, `filter()`.
16. Performance and `deque`.
17. Advanced exercises.

A useful teaching rule is to show the **difference between mutating an existing list and creating a new list** repeatedly. This single distinction explains many beginner mistakes.
