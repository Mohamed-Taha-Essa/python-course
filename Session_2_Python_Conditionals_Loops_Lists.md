# 🐍 Session 2 — Conditionals, Loops, and Lists

---

## 1. Quick Recap From Session 1

Before starting new topics, remember these core ideas:
- Variables store values: `name = "Ali"`
- Every value has a type: `str`, `int`, `float`, `bool`
- `input()` always returns text, so we convert it with `int()` or `float()` when needed
- Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) produce a boolean (`True` or `False`)

This session builds directly on that last point — booleans are what make decisions in code possible.

---

## 2. Conditional Statements

### Why do we need conditions?
So far, our programs run every line in order, no matter what. But real programs need to make decisions:
> "If the user is 18 or older, let them in. Otherwise, don't."

That's exactly what conditional statements do — they let a program choose which code to run based on whether something is `True` or `False`.

### The `if` statement
```python
age = 20

if age >= 18:
    print("You are an adult.")
```
How to read this: "If the condition `age >= 18` is `True`, run the code inside."

Notice two things:
- The line ends with a colon `:`
- The code that belongs to the `if` is **indented** (usually 4 spaces)

Indentation is not just style in Python — it's how Python knows which lines belong to the `if`. This is different from many other languages.

### The `if...else` statement
```python
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```
`else` runs when the `if` condition is `False`. Only one of the two blocks ever runs.

### The `if...elif...else` statement
Use `elif` (short for "else if") when there are more than two possible outcomes.
```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```
Python checks each condition from top to bottom and runs the **first** one that is `True`, then skips the rest.

### Nested conditions
An `if` statement can contain another `if` statement inside it.
```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("You need an ID.")
else:
    print("You are too young to enter.")
```

### Combining conditions with `and` / `or` / `not`
Instead of nesting, you can often combine conditions directly — this is usually easier to read.
```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")
else:
    print("Entry denied.")
```
```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today!")
```

### The ternary (short-form) `if`
For simple cases, you can write an `if...else` in one line:
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```
This is called a **ternary expression**. Use it only for short, simple decisions — for anything more complex, a regular `if` block is clearer.

### Common mistakes with conditionals

| Mistake | Wrong | Right |
|---|---|---|
| Forgetting the colon | `if age >= 18` | `if age >= 18:` |
| Wrong indentation | code not indented under `if` | indent consistently (usually 4 spaces) |
| Using `=` instead of `==` | `if age = 18:` | `if age == 18:` |
| Comparing with wrong logic | `if age >= 18 and age <= 12:` (impossible) | check your logic makes sense |

### 🧪 Try it
Write a program that asks for a number and prints whether it is positive, negative, or zero.

---

## 3. Loops

### Why do we need loops?
Imagine printing "Hello" five times:
```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```
That's repetitive and doesn't scale. Loops let us repeat code without rewriting it.

### The `for` loop
A `for` loop repeats code for each item in a sequence.
```python
for i in range(5):
    print("Hello")
```
This prints "Hello" 5 times.

### Understanding `range()`
`range()` generates a sequence of numbers.
```python
range(5)        # 0, 1, 2, 3, 4        → 5 numbers, starting at 0
range(1, 6)     # 1, 2, 3, 4, 5        → start and stop given
range(0, 10, 2) # 0, 2, 4, 6, 8        → start, stop, step
```
Example using the loop variable:
```python
for i in range(5):
    print(i)
```
Output:
```text
0
1
2
3
4
```
Notice `range(5)` stops **before** 5 — it never includes the stop value.

### Looping through a string
```python
word = "Python"

for letter in word:
    print(letter)
```
Output:
```text
P
y
t
h
o
n
```

### Looping through a list
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### The `while` loop
A `while` loop repeats code as long as a condition stays `True`.
```python
count = 0

while count < 5:
    print(count)
    count += 1
```
Output:
```text
0
1
2
3
4
```
Important: the condition must eventually become `False`, or the loop will run forever. This is called an **infinite loop** and is one of the most common beginner mistakes.
```python
# ❌ Infinite loop — count never changes
count = 0
while count < 5:
    print(count)
```

### `for` vs `while` — when to use which
- Use **`for`** when you know how many times to repeat, or you're going through a known sequence (a list, a string, a range of numbers).
- Use **`while`** when you don't know in advance how many times to repeat — you're repeating until some condition changes.

```python
# Good use of while: repeat until the user enters the right password
password = ""
while password != "python123":
    password = input("Enter the password: ")

print("Access granted.")
```

### `break` — stop the loop early
```python
for number in range(10):
    if number == 5:
        break
    print(number)
```
Output:
```text
0
1
2
3
4
```
As soon as `number == 5`, the loop stops completely.

### `continue` — skip to the next round
```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```
Output:
```text
0
1
3
4
```
`continue` skips the rest of the current round and moves to the next one — it doesn't stop the whole loop.

### `pass` — do nothing (a placeholder)
```python
for number in range(5):
    if number == 2:
        pass   # placeholder — does nothing, just avoids an error
    print(number)
```
`pass` is useful when Python requires a code block but you don't have code to put there yet.

### Nested loops
A loop can contain another loop inside it.
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```
Output:
```text
0 0
0 1
1 0
1 1
2 0
2 1
```
The inner loop completes fully for each single step of the outer loop.

### 🧪 Try it
1. Print all numbers from 1 to 10 using a `for` loop.
2. Print all even numbers from 1 to 20 using a `while` loop.
3. Use a loop and `if` together to print only the odd numbers from 1 to 10.

---

## 4. Lists and Basic Collections

Python has several built-in types for storing multiple values together. This session focuses mainly on **lists**, with a short look at the others.

| Collection | Ordered? | Changeable? | Allows duplicates? | Written as |
|---|---|---|---|---|
| `list` | Yes | Yes | Yes | `[1, 2, 3]` |
| `tuple` | Yes | No | Yes | `(1, 2, 3)` |
| `set` | No | Yes | No | `{1, 2, 3}` |
| `dict` | Yes (by insertion) | Yes | Keys are unique | `{"key": "value"}` |

---

### 4.1 Lists — The Basics

A list stores multiple values in a single variable, in order.
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Ali", 25, True, 3.14]   # lists can hold different types together
```

### Accessing items by index
Just like strings, list positions start at 0.
```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])    # apple
print(fruits[1])    # banana
print(fruits[-1])   # cherry (last item)
```

### Slicing a list
```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:3])   # [20, 30]
print(numbers[:2])    # [10, 20]
print(numbers[2:])    # [30, 40, 50]
print(numbers[::-1])  # [50, 40, 30, 20, 10]  → reversed
```

### Changing a list item
Unlike strings, lists **can** be changed after they're created (they are mutable).
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)   # ['apple', 'blueberry', 'cherry']
```

### Finding the length of a list
```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))   # 3
```

### Checking if something is in a list
```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      # True
print("mango" in fruits)       # False
```

---

### 4.2 Modifying Lists

### Adding items
```python
fruits = ["apple", "banana"]

fruits.append("cherry")          # adds to the end
print(fruits)   # ['apple', 'banana', 'cherry']

fruits.insert(1, "kiwi")         # adds at a specific position
print(fruits)   # ['apple', 'kiwi', 'banana', 'cherry']
```

### Removing items
```python
fruits = ["apple", "banana", "cherry"]

fruits.remove("banana")   # removes by value
print(fruits)   # ['apple', 'cherry']

fruits.pop()               # removes the last item (and returns it)
print(fruits)   # ['apple']

fruits.pop(0)               # removes item at a specific index
```

### Clearing a whole list
```python
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)   # []
```

### Sorting a list
```python
numbers = [5, 2, 8, 1, 9]

numbers.sort()
print(numbers)   # [1, 2, 5, 8, 9]

numbers.sort(reverse=True)
print(numbers)   # [9, 8, 5, 2, 1]
```

### Reversing a list
```python
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)   # [3, 2, 1]
```

### Copying a list correctly
```python
original = [1, 2, 3]
copy = original.copy()

copy.append(4)
print(original)   # [1, 2, 3]      → unchanged
print(copy)        # [1, 2, 3, 4]
```
Be careful — writing `copy = original` does **not** make a real copy. It just gives two names for the same list:
```python
original = [1, 2, 3]
not_a_copy = original     # both names point to the SAME list

not_a_copy.append(4)
print(original)   # [1, 2, 3, 4]   → changed too!
```

---

### 4.3 Looping Through Lists

### Basic loop
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### Loop with index using `enumerate()`
Sometimes you need both the position and the value.
```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```
Output:
```text
0 apple
1 banana
2 cherry
```

### Looping with conditions
```python
numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
```

---

### 4.4 List Comprehension (a shortcut for building lists)

A list comprehension is a compact way to create a new list from an existing one.

Normal way:
```python
numbers = [1, 2, 3, 4, 5]
squares = []

for n in numbers:
    squares.append(n ** 2)

print(squares)   # [1, 4, 9, 16, 25]
```

Same result with list comprehension:
```python
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)   # [1, 4, 9, 16, 25]
```

With a condition:
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)   # [2, 4, 6]
```

List comprehensions are optional and considered a more advanced style. It's good to recognize them, but writing a normal `for` loop is just as correct, especially while you're still learning.

---

### 4.5 Nested Lists

A list can contain other lists — this is often used to represent grids or tables.
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])       # [1, 2, 3]      → the first row
print(matrix[0][1])    # 2              → row 0, item at position 1
```

Looping through a nested list:
```python
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
```
Output:
```text
1 2 3
4 5 6
7 8 9
```

---

### 4.6 A Short Look at Other Collections

### Tuples — like lists, but unchangeable
```python
point = (10, 20)
print(point[0])   # 10

point[0] = 5   # ❌ TypeError — tuples cannot be changed
```
Tuples are useful when you want to make sure a group of values never changes, like fixed coordinates.

### Sets — unordered, no duplicates
```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)   # {1, 2, 3}   → duplicates are removed automatically
```
Sets are useful when you only care about unique values and don't need any particular order.

### Dictionaries — key/value pairs
```python
student = {
    "name": "Ali",
    "age": 20,
    "city": "Cairo"
}

print(student["name"])   # Ali
print(student["age"])    # 20
```
Dictionaries store data as labeled pairs instead of positions — very useful for representing real-world objects. Lists, tuples, sets, and dictionaries will all be explored in more depth in future sessions.

### 🧪 Try it
1. Create a list of 5 favorite movies and print them one by one using a `for` loop.
2. Add a new movie to the end of the list, then remove the first one.
3. Create a list of numbers from 1 to 10 and use a list comprehension to make a new list containing only the numbers greater than 5.

---

## 5. Putting It All Together

### Example: Grading Program
This combines conditionals, a loop, and a list.
```python
grades = [95, 82, 67, 45, 78]

for grade in grades:
    if grade >= 90:
        result = "A"
    elif grade >= 80:
        result = "B"
    elif grade >= 70:
        result = "C"
    elif grade >= 60:
        result = "D"
    else:
        result = "F"

    print(f"Grade {grade} → {result}")
```

### Example: Shopping List Checker
```python
shopping_list = ["milk", "bread", "eggs", "butter"]
budget = 50
prices = {"milk": 10, "bread": 5, "eggs": 8, "butter": 12}

total = 0
for item in shopping_list:
    total += prices[item]

if total <= budget:
    print(f"You can afford everything! Total: {total}")
else:
    print(f"Over budget! Total: {total}, Budget: {budget}")
```

### Example: Number Guessing Range Checker
```python
numbers = [3, 7, 12, 25, 40, 55, 8]

low = []
medium = []
high = []

for number in numbers:
    if number < 10:
        low.append(number)
    elif number < 30:
        medium.append(number)
    else:
        high.append(number)

print("Low:", low)
print("Medium:", medium)
print("High:", high)
```

---

## 6. Common Mistakes to Watch For

| Mistake | Wrong | Right |
|---|---|---|
| Forgetting the colon on loops | `for i in range(5)` | `for i in range(5):` |
| Wrong indentation inside loops/conditions | inconsistent spacing | keep indentation consistent (4 spaces) |
| Infinite `while` loop | condition variable never changes | update the variable inside the loop |
| Off-by-one errors with `range()` | expecting `range(5)` to include 5 | remember it stops *before* the stop value |
| Using `=` instead of `==` in a condition | `if x = 5:` | `if x == 5:` |
| Thinking `list2 = list1` makes a copy | changes to one affect both | use `list2 = list1.copy()` |
| Accessing an index that doesn't exist | `fruits[10]` on a 3-item list | check length with `len()` first, or use `in` |

---

## 7. What This Session Covered

By now, you should be able to:
- Use `if`, `elif`, and `else` to make decisions in code.
- Combine conditions with `and`, `or`, and `not`.
- Write a short conditional using the ternary form.
- Use `for` loops to repeat code a known number of times or go through a sequence.
- Use `while` loops to repeat code until a condition becomes false.
- Use `break`, `continue`, and `pass` to control loop behavior.
- Create, access, modify, and loop through lists.
- Use common list methods: `append`, `insert`, `remove`, `pop`, `sort`, `reverse`, `copy`.
- Recognize list comprehensions as a shortcut for building lists.
- Work with nested lists.
- Recognize tuples, sets, and dictionaries at a basic level.
- Combine conditionals, loops, and lists into small working programs.

---

## 8. Practice Before Next Session

1. Write a program that asks for a number and prints whether it's even or odd.
2. Write a program that prints the multiplication table (1 to 10) for a number the user enters.
3. Write a program that stores 5 numbers in a list and prints the largest and smallest value (without using `max()` or `min()`).
4. Write a program that asks the user to enter words one at a time (using a loop) until they type "stop", then prints the full list of words entered.
5. (Challenge) Write a program that stores a list of student names and grades (as two separate lists), then prints each student's name with "Pass" if their grade is 60 or above, or "Fail" otherwise.

---

## 9. Coming Up Next Session
- Functions — writing reusable blocks of code
- Function arguments and return values
- Working more deeply with dictionaries

---

## 📚 Extra Reading
- [Python official docs — control flow](https://docs.python.org/3/tutorial/controlflow.html)
- [W3Schools Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [GeeksforGeeks Python Loops](https://www.geeksforgeeks.org/python/python-loops/)
