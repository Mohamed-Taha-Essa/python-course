# 🐍 Session 1 — Introduction to Python Programming

---

## 1. What is Programming?

Programming means giving a computer clear, step-by-step instructions to do a task — like a recipe tells a cook what to do. A computer does not understand what you *want*. It only follows exact instructions.

For example, a person might say:
> "Calculate my average."

But a computer needs a precise process:
```text
1. Get the first grade.
2. Get the second grade.
3. Get the third grade.
4. Add the grades.
5. Divide the result by 3.
6. Show the average.
```

That list of steps is called an **algorithm**.

### Algorithm vs Program
- An **algorithm** is a logical sequence of steps for solving a problem.
- A **program** is that same sequence written in a programming language so a computer can run it.

Algorithm:
```text
Start
  ↓
Ask for name
  ↓
Ask for age
  ↓
Show name and age
  ↓
End
```

The same idea written as a Python program:
```python
name = input("Enter your name: ")
age = input("Enter your age: ")

print(name)
print(age)
```

This is an important idea: programming is not mainly about memorizing syntax. It's about three questions:
1. What problem am I solving?
2. What steps solve it?
3. How do I write those steps in Python?

---

## 2. What is Python?

Python is a **high-level**, **general-purpose** programming language.

**High-level** means it's written in a way that is fairly easy for humans to read, for example:
```python
total = price * quantity
```
This is much easier to understand than the low-level instructions a computer actually runs internally. Python hides that complexity so we can focus on solving problems.

**General-purpose** means Python is not limited to one kind of task. Python is used for:
- Web development
- Automation and scripting
- Data analysis
- Artificial intelligence and machine learning
- Scientific computing
- Testing
- Cybersecurity
- Desktop applications
- Education

Some popular Python tools and libraries you may hear about later: Django, Flask, FastAPI, NumPy, Pandas, PyTorch, TensorFlow. You don't need to know these yet — they just show why learning Python fundamentals is worth it.

### Why Python is Beginner-Friendly
Python's syntax is designed to read almost like plain English:
```python
name = "Ali"
print(name)
```
Python also has a large standard library, huge community, and countless learning resources.

But remember: Python being easy to *start* does not mean programming is always easy. The real challenge is learning to think logically and break problems into steps — not memorizing commands.

> "Python is like writing instructions in plain English for a fast, obedient, but very literal assistant."

---

## 3. Setting Up the Environment

### Option A — Install Python on your computer
1. Go to [python.org/downloads](https://python.org/downloads)
2. Download the latest Python 3.x version.
3. **Windows users:** check ✅ "Add Python to PATH" during install.
4. Check that it installed correctly by opening a terminal:
```bash
python --version
```
(On Mac/Linux it might be `python3 --version`)

### Option B — No install needed
- **Replit** ([replit.com](https://replit.com)) or **Google Colab** ([colab.research.google.com](https://colab.research.google.com)) — run Python in your browser, no setup needed.

### Choosing a code editor
- **VS Code** (recommended) — free and light, add the "Python" extension.
- **PyCharm Community** — more features, a bit heavier.
- **IDLE** — comes with Python, very simple.

---

## 4. How Python Runs Your Code

### The Python interpreter
The Python interpreter is the program that reads your code and actually runs it. It works like this:
```text
Python source code
        ↓
Python interpreter
        ↓
Execution
        ↓
Output
```
Whatever code you write, the interpreter is what turns it into real actions and results.

### The interactive shell (REPL)
You can run Python one line at a time by typing `python` (or `python3`) in a terminal. This opens an interactive shell, also called a **REPL**, which stands for:
- **R**ead
- **E**valuate
- **P**rint
- **L**oop

Example:
```python
>>> 2 + 3
5

>>> print("Hello")
Hello
```
The REPL is great for quick experiments and testing small pieces of code.

### Running a `.py` file
For real programs, you save your code in a file ending in `.py`, for example `hello.py`:
```python
print("Hello, Python!")
```
Then run it from the terminal:
```bash
python hello.py
```
or
```bash
python3 hello.py
```

**When to use which:**
- **Interactive shell** — quick experiments, testing small expressions, learning.
- **`.py` file** — real programs, saving your work, reusing code, building projects.

---

## 5. Your First Program

### The `print()` function
```python
print("Hello, World!")
```
This is your first working program.

### What happened?
- `print(...)` is a **function** — a ready-made block of code that does something (here: it shows text on the screen, also called "standard output").
- The text inside quotes `" "` is called a **string**.

### Printing text
```python
print("Mohamed")
print("Welcome to Python")
print("This is my first program")
```
Strings need quotes. Both single and double quotes work — just be consistent:
```python
print("Hello")
print('Hello')
```

### Printing numbers
```python
print(10)
print(25)
print(3.14)
```
Numbers don't need quotes. Compare:
```python
print(10)     # a number (integer)
print("10")   # a string (text)
```
They look the same on screen, but they are different kinds of values. This difference becomes very important soon.

### Printing expressions
Python can calculate something before printing the result:
```python
print(10 + 5)   # 15
print(10 - 3)
print(10 * 4)
print(10 / 2)
```
So `print()` doesn't just print text — it can also show the result of a calculation.

### Printing multiple values at once
```python
name = "Ali"
age = 20

print("Name:", name)
print("Age:", age)
print("Name:", name, "Age:", age)
```
Python automatically adds a space between each value separated by commas.

### Comments
Comments are notes in the code that Python skips. They are only for people to read.
```python
# This is a single-line comment
print("Comments help explain code")  # you can also add a comment after code

"""
This is a
multi-line comment
"""
```
Comments are most useful when they explain something that is not obvious — like *why* something is done, not just repeating what the code already says clearly.

Not very useful:
```python
# Store the name
name = "Ali"
```
More useful:
```python
# Convert the input to a number because input() always returns text
age = int(input("Enter your age: "))
```

### Common mistakes with `print()`
```python
print("Hello)      # ❌ missing closing quote
Print("Hello")     # ❌ Python cares about capital letters: 'Print' is not 'print'
print "Hello"      # ❌ missing parentheses (old Python 2 style, not used in Python 3)
```

### 🧪 Try it
Print your name and one fact about yourself using two separate `print()` lines.

---

## 6. Expressions

An **expression** is any piece of code that Python can evaluate to produce a value.

Examples:
```python
2 + 3
10 * 5
"Hello"
2 ** 3
```

Each one produces a result. For example:
```python
result = 5 + 4
```
The expression `5 + 4` produces `9`, and then `9` is stored in the variable `result`.

This idea matters because variables, calculations, and function outputs all depend on expressions producing values.

---

## 7. Variables

### Why do we need variables?
Imagine repeating the same value over and over:
```python
print("Mohamed")
print("Mohamed")
print("Mohamed")
```
What if that name needs to change everywhere? A variable lets us store a value once and refer to it by name:
```python
name = "Mohamed"

print(name)
print(name)
print(name)
```
Now the value is stored in one place.

### What is a variable?
A variable is a **name that stores a value**, so you can use it or change it later.

> Think of a variable like a labeled box. You put something inside it (`= value`), and later you can look inside it, use it, or put something new inside.

### Assignment: `=` is not "equals"
In math, `=` means "is equal to." In Python, `=` means **"store this value in this name."** This is one of the trickiest ideas for beginners, so take your time with it. Later, `==` will be used for comparing values — that's different.

```python
x = 5      # store 5 in x
x = x + 1  # take the current value of x, add 1, store the result back in x
print(x)   # 6
```

### Variables can change
```python
name = "Ahmed"
print(name)   # Ahmed

name = "Ali"
print(name)   # Ali
```
The variable now refers to the new value — the old one is replaced.

### Multiple variables
```python
name = "Ali"
age = 20
height = 1.75
student = True
```
This creates four names, each referring to its own value.

### Naming rules for variables
- Must start with a letter or underscore (`_`), not a number.
- Can have letters, numbers, and underscores — no spaces or symbols like `-`.
- Capital and lowercase letters are different (`name` and `Name` are not the same variable — Python is case-sensitive).
- Cannot be a Python keyword (`if`, `for`, `class`, etc.).
- Common style: use `snake_case` (`first_name`, not `FirstName`).

```python
age = 25          # ✅ good
_age = 25         # ✅ works, but not common
2age = 25         # ❌ not allowed — starts with a number
first name = 25   # ❌ not allowed — has a space
student-name = 25 # ❌ not allowed — the "-" is read as subtraction
```

Short names like `x`, `n`, `a` are fine for quick experiments, but for real programs, clear names are much easier to read:
```python
student_name = "Mohamed"   # ✅ clear
student_age = 20           # ✅ clear
```

### Storing many values at once
```python
x, y, z = 1, 2, 3
a = b = c = 10   # all three variables get the value 10
```

### Python figures out the type on its own
You never have to say what type a variable is ahead of time.
```python
score = 10       # score is a number right now
score = "high"   # now score is text — Python allows this
```

### 🧪 Try it
1. Make variables for `first_name`, `last_name`, `age`.
2. Print one sentence using all three, like: `print(first_name, last_name, "is", age, "years old")`.

---

## 8. Data Types

### The main built-in types

| Type | Example | What it is |
|------|---------|-------------|
| `str` | `name = "Lina"` | Text, inside `' '` or `" "` |
| `int` | `age = 25` | Whole numbers, positive or negative |
| `float` | `price = 19.99` | Numbers with a decimal point |
| `bool` | `is_active = True` | Only `True` or `False` |
| `NoneType` | `x = None` | Means "no value" |

### `str` — text
```python
name = "Mohamed"
city = "Cairo"
message = "Hello"
```

### `int` — whole numbers
```python
age = 31
students = 25
score = 100
```

### `float` — decimal numbers
```python
price = 99.99
height = 1.75
temperature = 36.5
```

### `bool` — True or False
```python
is_student = True
is_logged_in = False
```
Note that `True` and `False` (no quotes) are actual boolean values. `"True"` and `"False"` (with quotes) are just text — they are strings, not booleans.

### Checking a type with `type()`
`type()` tells you what kind of value something is:
```python
name = "Ali"
age = 20
price = 12.5
is_student = True

print(type(name))         # <class 'str'>
print(type(age))          # <class 'int'>
print(type(price))        # <class 'float'>
print(type(is_student))   # <class 'bool'>
```
This is very useful for understanding what's happening in your code, especially when something doesn't work the way you expect.

### True-like and false-like values
In Python, some values act like `True` or `False` even when they're not written that way:
- **Act like False:** `0`, `0.0`, `""` (empty text), `[]` (empty list), `None`, `False`
- **Act like True:** almost everything else (numbers that are not 0, text that is not empty, etc.)

```python
if "":
    print("This will not print")
if "hello":
    print("This will print")  # text that is not empty acts like True
```

### Changeable vs unchangeable types
- **Unchangeable (immutable):** `int`, `float`, `str`, `bool`, `tuple` — once made, the value inside cannot change.
- **Changeable (mutable):** `list`, `dict`, `set` — these come later.

### 🧪 Try it
Make one variable of each type (`int`, `float`, `str`, `bool`) and print both the value and its type using `type()`.

---

## 9. Getting Input From the User

### The `input()` function
```python
name = input("Enter your name: ")
print(name)
```
Here's what happens step by step:
```text
Program starts
    ↓
Python shows the prompt text
    ↓
User types a value
    ↓
User presses Enter
    ↓
input() returns what was typed
    ↓
The value is stored in the variable
```

### Important rule: `input()` always returns text
This is one of the most important beginner facts to remember:
```python
age = input("Enter your age: ")
```
Even if you type `20`, Python receives it as the text `"20"`, not the number `20`. So:
```python
print(type(age))   # <class 'str'>  — even though it looks like a number!
```
This surprises most beginners — it's the reason type conversion (next section) matters so much.

### 🧪 Try it
Ask for someone's name and print a greeting using it.

---

## 10. Type Conversion (Casting)

Type conversion means changing a value from one type to another.

### `int()` — convert to a whole number
```python
age = int("20")
print(age)           # 20
print(type(age))     # <class 'int'>
```
Common pattern with input:
```python
age = int(input("Enter your age: "))
```

### `float()` — convert to a decimal number
```python
price = float("19.99")
# or directly from input:
price = float(input("Enter price: "))
```

### `str()` — convert to text
```python
age = 20
message = "Age: " + str(age)
print(message)   # Age: 20
```

### Conversion is not always possible
This works:
```python
int("20")     # ✅ 20
```
This fails with an error:
```python
int("hello")  # ❌ cannot be converted to a number
```
Not every value can be converted to every type — this is normal and expected in programming.

### A common error
```python
age = "25"
print(age + 5)
# ❌ TypeError: can only concatenate str (not "int") to str
```
The fix:
```python
print(int(age) + 5)   # ✅ 30
```

### 🧪 Try it
Take two numbers written as text, turn them into whole numbers, and print their sum.

---

## 11. Strings vs Numbers

This is one of the most important ideas for beginners.

```python
print(10 + 5)       # 15   → numeric addition
print("10" + "5")   # 105  → string concatenation
```
Why the difference? `10 + 5` adds two numbers. `"10" + "5"` joins two pieces of text together — this is called **concatenation**.

```python
first_name = "Mohamed"
last_name = "Essa"

full_name = first_name + " " + last_name
print(full_name)   # Mohamed Essa
```

---

## 12. Operators

### Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor division | `5 // 2` | `2` |
| `%` | Modulo (remainder) | `5 % 2` | `1` |
| `**` | Power | `5 ** 2` | `25` |

Notes:
- `/` always gives a decimal result in Python, even if the numbers divide evenly: `10 / 2` gives `5.0`.
- `//` gives the whole-number part of the division, dropping anything after the decimal point.
- `%` gives the remainder after division. It's very useful for checking things like even/odd numbers:
```python
number = 10
print(number % 2)   # 0 → even

number = 11
print(number % 2)   # 1 → odd
```

### Assignment operators (shortcuts)
```python
x = 10
x += 5   # same as x = x + 5  → 15
x -= 2   # same as x = x - 2  → 13
x *= 2   # same as x = x * 2  → 26
x /= 2   # same as x = x / 2  → 13.0
```

### Order of operations (precedence)
Just like in math, Python follows an order: parentheses first, then powers, then multiply/divide, then add/subtract.
```python
result = 2 + 3 * 4      # 14, not 20 (multiplication happens first)
result2 = (2 + 3) * 4   # 20 (parentheses force addition first)
```
Use parentheses whenever they make your intention clearer — it costs nothing and avoids mistakes.

### Comparison operators
Comparison operators compare two values and always produce a boolean (`True` or `False`).
```python
print(10 > 5)    # True
print(10 < 5)    # False
print(10 >= 10)  # True
print(10 <= 10)  # True
print(10 == 10)  # True   → is equal to
print(10 != 5)   # True   → is not equal to
```

### `=` vs `==`
This is a very common beginner mix-up.
```python
age = 20      # assignment: store 20 in age
age == 20     # comparison: is age equal to 20?
```
A simple way to remember it:
```text
=   → store a value
==  → compare two values
```

### Logical operators
```python
age = 20
has_id = True

print(age >= 18 and has_id)   # True — both parts must be True
print(age >= 18 or has_id)    # True — at least one part is True
print(not has_id)             # False — flips True to False (or the other way)
```

### Membership operator (short preview)
```python
name = "Python"
print("P" in name)       # True
print("z" in name)       # False
```

### Boolean results and decisions
Comparisons producing `True`/`False` is the foundation for making decisions in code. Later, this connects to statements like:
```python
if age >= 18:
    print("Adult")
```
For now, the important part is getting comfortable with boolean thinking — expressions that evaluate to `True` or `False`.

### 🧪 Try it
Make a small calculator with two numbers: print their sum, difference, product, and quotient.

---

## 13. Strings in Detail

### Making strings
```python
s1 = "Hello"
s2 = 'World'
s3 = """This is a
multi-line string"""
```

### f-strings (the easiest way to build text with variables)
```python
name = "Lina"
age = 25
print(f"My name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1}.")   # you can also do math inside {}
```
The `f` before the quotes tells Python to evaluate whatever is inside `{}`.

### Indexing (getting one character by its position)
```python
word = "Python"
print(word[0])    # P   → counting starts at 0
print(word[1])    # y
print(word[-1])   # n   → negative numbers count from the end
```

### Slicing (getting part of a string)
```python
word = "Python"
print(word[0:2])   # 'Py'   → from index 0 up to (not including) 2
print(word[2:])    # 'thon' → from index 2 to the end
print(word[:2])    # 'Py'   → from the start up to index 2
print(word[::-1])  # 'nohtyP' → reverses the string
```

### String length
```python
print(len("Python"))   # 6
```

### Useful string methods
```python
s = "  Hello World  "
print(s.upper())        # "  HELLO WORLD  "
print(s.lower())        # "  hello world  "
print(s.strip())        # "Hello World"   (removes extra spaces at start/end)
print(s.replace("World", "Python"))  # "  Hello Python  "
print(s.split())        # ['Hello', 'World']  → breaks into a list of words
print("Py" in "Python") # True
print(s.strip().startswith("Hello"))  # True
```

### Strings cannot be changed directly
```python
word = "Python"
word[0] = "J"   # ❌ TypeError: 'str' object does not support item assignment
word = "Jython" # ✅ you can only make a brand new string, not edit the old one
```

### 🧪 Try it
1. Store your full name in a variable.
2. Print it in uppercase.
3. Print just the first 3 letters using slicing.
4. Print the length of your name.
5. Use an f-string to print: `"My name has X letters."`

---

## 14. Common Mistakes to Watch For

| Mistake | Wrong | Right |
|---|---|---|
| Forgetting quotes | `print(Hello)` | `print("Hello")` |
| Confusing `=` and `==` | `age == 20` (when assigning) | `age = 20` |
| Forgetting input conversion | `age = input(...); print(age + 1)` | `age = int(input(...)); print(age + 1)` |
| Mixing text and numbers incorrectly | `print("Age: " + age)` | `print(f"Age: {age}")` or `print("Age: " + str(age))` |
| Invalid variable names | `student-name = "Ali"` | `student_name = "Ali"` |
| Ignoring case sensitivity | `name = "Ali"; print(Name)` | `print(name)` |

---

## 15. Understanding Python Errors

Errors are a normal part of programming — they're information, not failure. Here are three common ones you'll see early on:

### Syntax Error
```python
print("Hello"
```
This means Python cannot understand the structure of the code — here, a closing parenthesis is missing.

### Name Error
```python
print(name)
```
This happens when `name` has never been created (assigned a value). Python doesn't know what it refers to.

### Value Error
```python
age = int("hello")
```
This happens when a value cannot be converted to the requested type — `"hello"` cannot become a number.

Reading the error message carefully usually tells you exactly what went wrong and where.

---

## 16. The Big Picture

A small Python program already uses most of the ideas from this session:
```text
                PYTHON PROGRAM

                     INPUT
                       ↓
                input("...")
                       ↓
              string/text value
                       ↓
              type conversion
              int() / float()
                       ↓
                  VARIABLES
                       ↓
                OPERATIONS
          + - * / // % ** == > <
                       ↓
                  RESULT
                       ↓
                   print()
                       ↓
                    OUTPUT
```

For example:
```python
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Total: {total}")
```

---

## 17. Practice Projects

### Profile Card Generator
This example uses everything from today — variables, input, type conversion, string methods, f-strings, and operators.
```python
name = input("What is your name? ")
age = int(input("What is your age? "))
city = input("What city do you live in? ")

print("=" * 30)
print(f"👤 NAME: {name.upper()}")
print(f"🎂 AGE: {age}")
print(f"📍 CITY: {city.title()}")
print(f"➕ In 10 years you'll be {age + 10} years old.")
print("=" * 30)
```

### Student Average Calculator
This example asks for a name, age, and three grades, then calculates the average.
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

grade1 = float(input("Enter first grade: "))
grade2 = float(input("Enter second grade: "))
grade3 = float(input("Enter third grade: "))

average = (grade1 + grade2 + grade3) / 3

print()
print("===== Student Information =====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Average: {average}")
```

---

## 18. Practice Before Next Session

1. Write a program that asks for two numbers and prints their sum, difference, product, division, floor division, and remainder.
2. Write a program that asks for a first and last name and prints them combined in uppercase.
3. Write a program that asks for a sentence and prints: its length, the first word (using slicing or split), and the sentence reversed.
4. Write a Celsius-to-Fahrenheit converter using the formula `F = (C × 9/5) + 32`.
5. (Challenge) Build your own version of the Profile Card Generator with at least 2 extra pieces of information.

---

## 19. What This Session Covered

By now, you should be able to:
- Explain what programming and an algorithm are.
- Explain what Python is and where it's used.
- Run Python code from a terminal and from a `.py` file.
- Use `print()` to display text, numbers, and expressions.
- Write comments.
- Recognize strings, integers, floats, and booleans.
- Create and use variables.
- Use `type()` to check a value's type.
- Read user input with `input()`.
- Convert values using `int()`, `float()`, and `str()`.
- Use arithmetic, comparison, and logical operators.
- Work with strings in detail: concatenation, f-strings, indexing, slicing, and methods.
- Recognize and understand common beginner errors.
- Combine all of this into a small working program.

---

## 20. Coming Up Next Session
- Conditional statements (`if`, `elif`, `else`)
- Loops (`for`, `while`)
- Lists and basic collections

---

## 📚 Extra Reading
- [Python official docs](https://docs.python.org/3/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [GeeksforGeeks Python Basics](https://www.geeksforgeeks.org/python/python-syllabus/)
