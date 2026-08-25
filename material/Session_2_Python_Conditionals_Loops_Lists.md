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

## 3. Switch-Style Decisions: `match` — `case`

### Why not just use `if...elif...else` for everything?
You can — `if...elif...else` always works. But when you're checking **one single value** against many possible exact matches, a long `elif` chain can get repetitive:
```python
day = "Mon"

if day == "Mon":
    print("Monday")
elif day == "Tue":
    print("Tuesday")
elif day == "Wed":
    print("Wednesday")
else:
    print("Unknown day")
```
Many programming languages have a `switch` statement for exactly this situation. Python's version is called `match...case`, introduced in Python 3.10.

### Basic `match` syntax
```python
day = "Mon"

match day:
    case "Mon":
        print("Monday")
    case "Tue":
        print("Tuesday")
    case "Wed":
        print("Wednesday")
    case _:
        print("Unknown day")
```
- `match day:` starts checking the value of `day`.
- Each `case` is one possible value to compare against.
- `case _:` is the **default case** — it matches anything not caught above (similar to `else`).

### Matching multiple values in one case
```python
day = "Sat"

match day:
    case "Sat" | "Sun":
        print("Weekend")
    case "Mon" | "Tue" | "Wed" | "Thu" | "Fri":
        print("Weekday")
    case _:
        print("Unknown day")
```
The `|` symbol means "or" — the case matches if the value equals any of the listed options.

### `match` with numbers
```python
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status code")
```

### Real scenario: order status
```python
order_status = "shipped"

match order_status:
    case "pending":
        print("Your order is being prepared.")
    case "shipped":
        print("Your order is on its way.")
    case "delivered":
        print("Your order has arrived.")
    case "cancelled":
        print("Your order was cancelled.")
    case _:
        print("Unknown order status.")
```

### If `match` is not available
`match...case` needs Python 3.10 or newer. If you're using an older version, the standard `if...elif...else` chain does exactly the same job — it's just a bit longer to type. Both are correct; `match` is simply a cleaner option for this specific pattern (one value, many exact possibilities).

### 🧪 Try it
Write a program using `match` that takes a traffic light color (`"red"`, `"yellow"`, `"green"`) and prints what a driver should do.

---

## 4. Handling Errors: `try` and `except`

### What is an exception?
An exception is an error that happens **while the program is running**. Unlike a syntax error (which stops the program before it even starts), an exception happens in the middle of execution — often because of unexpected input.
```python
age = int("hello")
# ❌ ValueError: invalid literal for int() with base 10: 'hello'
```
Without handling, this error crashes the whole program.

### The `try...except` block
`try...except` lets your program catch an error and respond to it, instead of crashing.
```python
try:
    age = int(input("Enter your age: "))
    print(f"Next year you will be {age + 1}")
except ValueError:
    print("That's not a valid number.")
```
How to read this: "**Try** to run this code. If a `ValueError` happens, **except** — run this other code instead."

### Catching different error types
Different mistakes cause different exception types. You can handle them separately.
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

### Catching any error (use carefully)
```python
try:
    result = 10 / 0
except Exception as e:
    print("Something went wrong:", e)
```
This catches almost any error. It's useful for a last-resort safety net, but catching *specific* errors (like `ValueError`, `ZeroDivisionError`) is usually better, because it helps you understand exactly what went wrong.

### `else` — runs only if no error happened
```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
else:
    print("You entered:", number)
```

### `finally` — always runs, error or not
```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
finally:
    print("Program finished.")
```
`finally` is useful for cleanup steps that must happen no matter what — for example, closing a file or a connection.

### Common exception types to recognize

| Exception | When it happens |
|---|---|
| `ValueError` | A value has the right type but the wrong content, e.g. `int("hello")` |
| `TypeError` | An operation is used on the wrong type, e.g. `"5" + 5` |
| `ZeroDivisionError` | Dividing a number by zero |
| `IndexError` | Accessing a list position that doesn't exist |
| `KeyError` | Accessing a dictionary key that doesn't exist |
| `NameError` | Using a variable that was never created |

### Real scenario: safe input loop
This keeps asking until the user enters a valid number — a very common real-world pattern.
```python
while True:
    try:
        quantity = int(input("Enter quantity: "))
        break
    except ValueError:
        print("Please enter a whole number.")

print(f"You ordered {quantity} item(s).")
```

### 🧪 Try it
Write a program that asks the user for two numbers and divides the first by the second. Use `try...except` to handle both invalid input and division by zero.

---

## 5. Advanced Real-Scenario Example: E-Commerce Order Processor

This example combines everything so far: `if/elif`, `match`, `try/except`, and loops — in one realistic mini-program.
```python
orders = ["5", "abc", "0", "3", "-2"]

for order in orders:
    print(f"\nProcessing order quantity: {order}")

    try:
        quantity = int(order)

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

    except ValueError as e:
        print(f"Invalid order skipped: {e}")
        continue

    # Determine shipping type based on quantity
    match True:
        case _ if quantity >= 10:
            shipping = "Bulk Freight"
        case _ if quantity >= 5:
            shipping = "Standard Shipping"
        case _:
            shipping = "Small Package"

    price_per_item = 25
    total = quantity * price_per_item

    if total >= 100:
        discount = total * 0.10
        total -= discount
        print(f"Discount applied: -{discount}")

    print(f"Quantity: {quantity} | Shipping: {shipping} | Total: ${total}")
```
What this program does, step by step:
1. Loops through a list of raw order quantities (some invalid on purpose).
2. Uses `try/except` to safely convert each one to a number, skipping bad values with `continue`.
3. Uses `match` with a condition-based pattern to decide the shipping type.
4. Uses `if` to apply a discount for large orders.
5. Prints a clear summary for every valid order.

This is close to how real order-processing logic works: validate first, then decide, then calculate.

---

## 6. Loops

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

## 7. Lists — Complete Reference

### What is a list?
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

### Checking if something is in a list
```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      # True
print("mango" in fruits)       # False
```

---

### 7.1 Every Built-in List Method, in Detail

Python lists come with 11 built-in methods. Here is every one of them, with what it does, its parameters, what it returns, and a real-scenario example.

#### `append(item)`
Adds one item to the **end** of the list. Changes the list in place, returns `None`.
```python
cart = ["shoes", "shirt"]
cart.append("hat")
print(cart)   # ['shoes', 'shirt', 'hat']
```
Real scenario — adding a new item to a shopping cart when the user clicks "Add to Cart":
```python
cart = []
cart.append("wireless mouse")
print(cart)   # ['wireless mouse']
```

#### `extend(iterable)`
Adds **all items** from another list (or any iterable) to the end of the list — unlike `append`, which would add the whole list as a single item.
```python
cart = ["shoes"]
new_items = ["shirt", "hat"]

cart.extend(new_items)
print(cart)   # ['shoes', 'shirt', 'hat']
```
Compare with `append` (common mistake):
```python
cart = ["shoes"]
cart.append(["shirt", "hat"])
print(cart)   # ['shoes', ['shirt', 'hat']]   ❌ probably not what you wanted
```
Real scenario — merging a new batch of followers into an existing followers list:
```python
followers = ["ali_92", "sara_x"]
new_followers = ["mo_dev", "lina.k"]

followers.extend(new_followers)
print(followers)   # ['ali_92', 'sara_x', 'mo_dev', 'lina.k']
```

#### `insert(index, item)`
Adds an item at a **specific position**, shifting the rest of the items to the right.
```python
cart = ["shoes", "hat"]
cart.insert(1, "shirt")
print(cart)   # ['shoes', 'shirt', 'hat']
```
Real scenario — pinning a post to the top of a feed (index 0):
```python
feed = ["post_102", "post_101", "post_100"]
feed.insert(0, "pinned_post_999")
print(feed)   # ['pinned_post_999', 'post_102', 'post_101', 'post_100']
```

#### `remove(item)`
Removes the **first** matching value from the list. If the value doesn't exist, it raises a `ValueError`.
```python
cart = ["shoes", "shirt", "shoes"]
cart.remove("shoes")
print(cart)   # ['shirt', 'shoes']   → only the first match is removed
```
Real scenario — a user unfollows one account:
```python
following = ["tech_news", "daily_memes", "cooking101"]
following.remove("daily_memes")
print(following)   # ['tech_news', 'cooking101']
```
Safer version using `try/except` in case the value isn't there:
```python
try:
    following.remove("not_a_real_account")
except ValueError:
    print("That account wasn't in the following list.")
```

#### `pop(index=-1)`
Removes and **returns** the item at a given position. If no index is given, it removes the **last** item.
```python
cart = ["shoes", "shirt", "hat"]

last_item = cart.pop()
print(last_item)   # hat
print(cart)         # ['shoes', 'shirt']

first_item = cart.pop(0)
print(first_item)   # shoes
print(cart)          # ['shirt']
```
Real scenario — processing the next order in a queue, one at a time:
```python
order_queue = ["order_1", "order_2", "order_3"]

next_order = order_queue.pop(0)
print(f"Now processing: {next_order}")
print("Remaining queue:", order_queue)
```

#### `clear()`
Removes **all** items, leaving an empty list.
```python
cart = ["shoes", "shirt", "hat"]
cart.clear()
print(cart)   # []
```
Real scenario — emptying a shopping cart after checkout:
```python
cart = ["laptop", "mouse", "keyboard"]
print("Order placed for:", cart)
cart.clear()
print("Cart after checkout:", cart)   # []
```

#### `index(item, start=0, end=len(list))`
Returns the position of the **first** matching value. Raises a `ValueError` if the item isn't found.
```python
fruits = ["apple", "banana", "cherry"]
position = fruits.index("banana")
print(position)   # 1
```
Real scenario — finding where a specific product sits in a list of trending products:
```python
trending = ["phone_case", "earbuds", "charger", "earbuds"]
position = trending.index("earbuds")
print(f"'earbuds' first appears at position {position}")
```

#### `count(item)`
Returns **how many times** a value appears in the list.
```python
votes = ["yes", "no", "yes", "yes", "no"]
print(votes.count("yes"))   # 3
print(votes.count("no"))    # 2
```
Real scenario — counting how many times a hashtag appears in a list of posts:
```python
hashtags = ["#travel", "#food", "#travel", "#fitness", "#travel"]
print(f"#travel was used {hashtags.count('#travel')} times")
```

#### `sort(key=None, reverse=False)`
Sorts the list **in place** (changes the original list, returns `None`). By default, sorts in ascending order.
```python
prices = [49.99, 9.99, 120.50, 25.00]
prices.sort()
print(prices)   # [9.99, 25.0, 49.99, 120.5]

prices.sort(reverse=True)
print(prices)   # [120.5, 49.99, 25.0, 9.99]
```
Using `key` to sort by something specific — for example, sorting product names by length:
```python
products = ["TV", "Smartphone", "Fan", "Refrigerator"]
products.sort(key=len)
print(products)   # ['TV', 'Fan', 'Smartphone', 'Refrigerator']
```
Real scenario — sorting posts by number of likes, most popular first:
```python
likes = [340, 12, 987, 56]
likes.sort(reverse=True)
print(likes)   # [987, 340, 56, 12]
```

#### `reverse()`
Reverses the order of the list **in place**.
```python
history = ["visited_home", "visited_shop", "visited_cart"]
history.reverse()
print(history)   # ['visited_cart', 'visited_shop', 'visited_home']
```
Real scenario — showing a user's browsing history with the most recent page first.

#### `copy()`
Returns a **new, independent copy** of the list (a shallow copy).
```python
original_cart = ["shoes", "shirt"]
backup_cart = original_cart.copy()

backup_cart.append("hat")
print(original_cart)   # ['shoes', 'shirt']       → unchanged
print(backup_cart)      # ['shoes', 'shirt', 'hat']
```
Be careful — writing `backup = original` does **not** make a real copy. Both names point to the same list:
```python
original_cart = ["shoes", "shirt"]
not_a_copy = original_cart     # same list, two names

not_a_copy.append("hat")
print(original_cart)   # ['shoes', 'shirt', 'hat']   → changed too!
```

### 7.2 Summary Table of List Methods

| Method | What it does | Changes original? | Returns |
|---|---|---|---|
| `append(item)` | Adds one item to the end | Yes | `None` |
| `extend(iterable)` | Adds multiple items to the end | Yes | `None` |
| `insert(i, item)` | Adds an item at a specific position | Yes | `None` |
| `remove(item)` | Removes first matching value | Yes | `None` |
| `pop(i)` | Removes and returns item at position (default last) | Yes | the removed item |
| `clear()` | Removes all items | Yes | `None` |
| `index(item)` | Finds the position of a value | No | the index (int) |
| `count(item)` | Counts how many times a value appears | No | the count (int) |
| `sort()` | Sorts the list | Yes | `None` |
| `reverse()` | Reverses the list order | Yes | `None` |
| `copy()` | Makes an independent copy | No | a new list |

### 7.3 Built-in Functions That Work Well With Lists
These are not list *methods* (you don't write `list.function()`), but standalone functions that accept a list as input — very useful to know alongside the methods above.
```python
numbers = [4, 8, 15, 16, 23, 42]

print(len(numbers))       # 6      → number of items
print(sum(numbers))       # 108    → total of all items
print(max(numbers))       # 42     → largest item
print(min(numbers))       # 4      → smallest item
print(sorted(numbers))    # [4, 8, 15, 16, 23, 42]  → NEW sorted list, original unchanged
print(list(reversed(numbers)))  # [42, 23, 16, 15, 8, 4]
```
The key difference from `.sort()` and `.reverse()`: `sorted()` and `reversed()` do **not** change the original list — they give you a new result instead.

### 7.4 Looping Through Lists

#### Basic loop
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

#### Loop with index using `enumerate()`
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

#### Looping with conditions
```python
numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
```

### 7.5 List Comprehension (a shortcut for building lists)

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

### 7.6 Nested Lists

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

### 7.7 A Short Look at Other Collections

#### Tuples — like lists, but unchangeable
```python
point = (10, 20)
print(point[0])   # 10

point[0] = 5   # ❌ TypeError — tuples cannot be changed
```
Tuples are useful when you want to make sure a group of values never changes, like fixed coordinates.

#### Sets — unordered, no duplicates
```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)   # {1, 2, 3}   → duplicates are removed automatically
```
Sets are useful when you only care about unique values and don't need any particular order.

#### Dictionaries — key/value pairs
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

## 8. Putting It All Together

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

### Example: Number Range Checker
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

## 9. Common Mistakes to Watch For

| Mistake | Wrong | Right |
|---|---|---|
| Forgetting the colon on loops | `for i in range(5)` | `for i in range(5):` |
| Wrong indentation inside loops/conditions | inconsistent spacing | keep indentation consistent (4 spaces) |
| Infinite `while` loop | condition variable never changes | update the variable inside the loop |
| Off-by-one errors with `range()` | expecting `range(5)` to include 5 | remember it stops *before* the stop value |
| Using `=` instead of `==` in a condition | `if x = 5:` | `if x == 5:` |
| Confusing `append` and `extend` | `cart.append(["a","b"])` | `cart.extend(["a","b"])` |
| Thinking `list2 = list1` makes a copy | changes to one affect both | use `list2 = list1.copy()` |
| Accessing an index that doesn't exist | `fruits[10]` on a 3-item list | check length with `len()` first, or use `in` |
| Not catching the right exception | bare `except:` for everything | catch specific errors like `ValueError` |

---

## 10. What This Session Covered

By now, you should be able to:
- Use `if`, `elif`, and `else` to make decisions in code.
- Combine conditions with `and`, `or`, and `not`.
- Write a short conditional using the ternary form.
- Use `match...case` as a cleaner alternative to long `elif` chains.
- Use `try`, `except`, `else`, and `finally` to handle runtime errors safely.
- Recognize common exception types: `ValueError`, `TypeError`, `ZeroDivisionError`, `IndexError`, `KeyError`, `NameError`.
- Use `for` loops to repeat code a known number of times or go through a sequence.
- Use `while` loops to repeat code until a condition becomes false.
- Use `break`, `continue`, and `pass` to control loop behavior.
- Create, access, modify, and loop through lists.
- Use every built-in list method: `append`, `extend`, `insert`, `remove`, `pop`, `clear`, `index`, `count`, `sort`, `reverse`, `copy`.
- Use built-in functions that work with lists: `len()`, `sum()`, `max()`, `min()`, `sorted()`, `reversed()`.
- Recognize list comprehensions as a shortcut for building lists.
- Work with nested lists.
- Recognize tuples, sets, and dictionaries at a basic level.
- Combine conditionals, loops, error handling, and lists into small working programs.

---

## 11. Coming Up Next Session
- Functions — writing reusable blocks of code
- Function arguments and return values
- Working more deeply with dictionaries

---

## 📚 Extra Reading
- [Python official docs — control flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Python official docs — errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
- [W3Schools Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [GeeksforGeeks Python Loops](https://www.geeksforgeeks.org/python/python-loops/)

---

## 12. Practice Tasks — Basic to Advanced

These tasks are based on real-world scenarios from social media and e-commerce apps — the same kind of logic used in real products. Work through them in order; each one builds on ideas from the tasks before it.

### Task 1 (Basic) — Cart Total
An online store sells one product at **$25** each. Ask the user how many units they want to buy, then print the total price.

### Task 2 (Basic) — Follower Check
You are given a list of usernames who follow an account:
```python
followers = ["ali_92", "sara_x", "mo_dev", "lina.k"]
```
Ask the user to type a username, then print whether that username is in the followers list.

### Task 3 (Basic–Medium) — Safe Quantity Input
Ask the user to enter the quantity of a product they want to order. Use `try/except` to make sure the program doesn't crash if they type something that isn't a number — instead, print a friendly message and ask again.

### Task 4 (Medium) — Popular Posts Counter
You are given a list of like-counts for a user's posts:
```python
likes = [45, 230, 12, 987, 56, 1200, 3]
```
Loop through the list and count how many posts have more than 100 likes. Print the final count.

### Task 5 (Medium) — Order Status Messages
Using `match...case`, write a program that takes an order status (`"pending"`, `"shipped"`, `"delivered"`, `"cancelled"`) and prints an appropriate message for the customer, plus a default message for any other status.

### Task 6 (Medium) — Unfollow a User
You are given a list of accounts a user follows:
```python
following = ["tech_news", "daily_memes", "cooking101", "travel_diaries"]
```
Ask the user which account they want to unfollow. If it exists in the list, remove it and print the updated list. If it doesn't exist, print a message saying so — without crashing the program.

### Task 7 (Medium–Advanced) — Shopping Cart With Free Shipping
You are given a list of item prices already in a user's cart:
```python
cart = [15.99, 42.50, 9.75, 60.00]
```
Calculate the total. If the total is **$100 or more**, apply free shipping and print a message saying so. Otherwise, print the shipping fee as **$5.99** added to the total.

### Task 8 (Advanced) — Active Users Filter
You are given two lists — usernames and whether each one is currently online:
```python
usernames = ["ali_92", "sara_x", "mo_dev", "lina.k"]
is_online = [True, False, True, True]
```
Using a loop (or a list comprehension if you'd like to try it), build a new list containing only the usernames that are currently online, and print it.

### Task 9 (Advanced) — Processing Multiple Orders Safely
You are given a list of raw order quantities, some of them invalid:
```python
raw_orders = ["4", "two", "0", "-1", "10", ""]
```
Loop through the list. For each value, use `try/except` to convert it to a number. If the conversion fails, or the number is zero or negative, skip that order using `continue` and print a message saying it was invalid. For every valid order, print the quantity and the total cost at **$20 per item**.

### Task 10 (Capstone) — Social Media Post Analytics
You are given a list of like-counts from a user's last 10 posts:
```python
post_likes = [1200, 45, 980, 15, 3400, 220, 0, 87, 5600, 12]
```
Write a program that:
1. Uses `try/except` to safely handle the case where the list might be empty (calculate the average only if there is at least one post).
2. Calculates and prints the **total** likes and the **average** likes per post.
3. Loops through the list and, for each post, prints whether it is `"Viral"` (1000+ likes), `"Popular"` (100–999 likes), or `"Normal"` (under 100 likes) — using `if/elif/else`.
4. Finds and prints the **highest** number of likes and which post (by position) achieved it, without using `max()`.
