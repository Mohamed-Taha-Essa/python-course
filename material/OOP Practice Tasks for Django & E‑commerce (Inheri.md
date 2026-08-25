<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# OOP Practice Tasks for Django \& E‑commerce (Inheritance, Polymorphism, Encapsulation)

This file contains **real-world–style tasks** designed to help your students **learn and apply** OOP concepts (inheritance, polymorphism, encapsulation) in contexts they will actually meet: **Django projects** and **e‑commerce systems**.[^1][^2][^3][^4]

Each task includes:

- A short scenario
- Learning goals (which OOP concepts are practiced)
- Requirements
- Stretch goals (optional challenges)
- Notes on how this maps to Django

You can assign **one big task** (e.g., Task 2 or 3) or **several smaller ones** (Task 1 + 2).

***

## How to use these tasks

- Ask students to implement the core logic in **plain Python first** (no Django required).
- Then, as a follow-up, have them **translate the design into Django models** where applicable.
- Encourage them to write **tests** (even simple `assert` checks) to verify behavior.
- Emphasize **why** a design decision is made (e.g., “we use inheritance here because…”).[^5][^1]

***

## Task 1 — Product Catalog with Discounts (Core OOP + E‑commerce)

### Scenario

You are building the backend for a small online store. The store sells different types of products (electronics, clothing, groceries). Each product has a price, but **discount rules differ by category**. You also need to **protect sensitive data** (like cost price) and expose only what’s needed.

### Learning goals

- **Encapsulation**: hide internal attributes, expose controlled access.
- **Inheritance**: create specialized product types from a base `Product`.
- **Polymorphism**: apply discounts and display details differently per product type.[^2][^4][^1]


### Requirements

1. Create a base class `Product`:
    - Attributes (some should be “private” by convention):
        - `_name` (str)
        - `_price` (float) – selling price
        - `_cost_price` (float) – internal, should not be accessed directly
    - Methods:
        - `name` property (read-only)
        - `price` property (read-only)
        - `get_profit_margin()` → returns `price - cost_price`
        - `apply_discount()` → base implementation (e.g., no discount or a small default)
        - `display_details()` → returns a string with basic info
2. Create at least **two subclasses**:
    - `ElectronicItem(Product)`
        - Extra attribute: `warranty_months`
        - Override `apply_discount()` → e.g., 10% off
        - Override `display_details()` → include warranty info
    - `ClothingItem(Product)`
        - Extra attribute: `size` (e.g., "M", "L")
        - Override `apply_discount()` → e.g., 20% off
        - Override `display_details()` → include size info
3. Create a simple `Cart` class:
    - Holds a list of `(product, quantity)` pairs.
    - Methods:
        - `add_item(product: Product, quantity: int)`
        - `get_total()` → sum of `product.price * quantity` after applying each product’s discount logic via `apply_discount()`.
        - `view_cart()` → prints each item with its details (use `display_details()`).
4. Demonstrate **polymorphism**:
    - In `Cart.get_total()`, call `product.apply_discount()` without checking the product type. The correct discount logic should run based on the actual class.[^3][^4][^2]

### Example usage (for students to aim for)

```python
laptop = ElectronicItem("Laptop", 1000, 800, warranty_months=24)
shirt = ClothingItem("T-Shirt", 30, 12, size="L")

cart = Cart()
cart.add_item(laptop, 1)
cart.add_item(shirt, 2)

print(cart.view_cart())
print("Total:", cart.get_total())
```


### Stretch goals

- Add a `GroceryItem(Product)` with `expiry_date` and a discount that increases as the expiry date approaches.
- Add a `Coupon` class that can be applied to the entire cart (e.g., 5% off total).
- Use **abstract base classes** (`abc.ABC`) to enforce that all products implement `apply_discount()` and `display_details()`.[^4][^3]


### Django mapping notes

- In Django, `Product`, `ElectronicItem`, etc. could become **models** using **model inheritance** (abstract base class for common fields).[^6][^7][^8]
- `apply_discount()` logic might move to model methods or service functions, but the OOP design remains similar.

***

## Task 2 — User Roles \& Permissions (Django‑style OOP)

### Scenario

You are designing a system that supports different user roles: **Customer**, **Vendor**, and **Admin**. All users share some data (username, email, password), but each role has **different permissions** and **extra attributes**. You want to model this cleanly using OOP, similar to how you’d design custom user models in Django.[^9][^10][^6]

### Learning goals

- **Inheritance**: share common user fields in a base class, extend for roles.
- **Encapsulation**: protect password and sensitive fields.
- **Polymorphism**: role-specific behavior through overridden methods.[^11][^1][^5]


### Requirements

1. Create a base class `User`:
    - Attributes:
        - `_username`
        - `_email`
        - `_password` (should not be directly accessible)
    - Methods:
        - Properties for `username` and `email` (read-only or with validation).
        - `check_password(plain: str) -> bool` → compare with stored password (you can simulate hashing).
        - `get_role_name() -> str` → returns generic role name (e.g., "User").
        - `can_access(resource: str) -> bool` → base implementation (default: deny most things).
2. Create subclasses:
    - `Customer(User)`
        - Extra attribute: `shipping_address`
        - Override `get_role_name()` → "Customer".
        - Override `can_access(resource)` → allow access to `"products"`, `"orders"`, `"profile"`.
    - `Vendor(User)`
        - Extra attributes: `store_name`, `is_verified`
        - Override `get_role_name()` → "Vendor".
        - Override `can_access(resource)` → allow `"products"`, `"orders"`, `"dashboard"`, `"analytics"`.
    - `Admin(User)`
        - Extra attribute: `admin_level` (e.g., 1–3)
        - Override `get_role_name()` → "Admin".
        - Override `can_access(resource)` → allow almost everything, maybe restrict some high-level resources based on `admin_level`.
3. Create a simple `ResourceGuard` class:
    - Method: `access_allowed(user: User, resource: str) -> bool`
    - Uses `user.can_access(resource)` to decide.
    - Demonstrate **polymorphism**: same method call, different behavior depending on user type.[^1][^11]

### Example usage

```python
customer = Customer("ali", "ali@example.com", "secret123", "Cairo, St 1")
admin = Admin("sara", "sara@example.com", "adminpass", admin_level=3)

guard = ResourceGuard()

print(guard.access_allowed(customer, "products"))  # True
print(guard.access_allowed(customer, "analytics")) # False
print(guard.access_allowed(admin, "analytics"))    # True
```


### Stretch goals

- Add a `Staff(User)` role with limited admin rights.
- Implement a method `get_dashboard_url()` that returns different URLs per role (polymorphism).
- Add simple **validation** in setters (e.g., email format, non-empty username).[^10][^5]


### Django mapping notes

- This mirrors Django’s **custom user model** patterns and role-based permissions.[^6][^9]
- In Django, you might use a single `User` model with a `role` field and permission groups, but the OOP exercise helps students understand the underlying design.

***

## Task 3 — Payment System with Multiple Providers (Polymorphism + Encapsulation)

### Scenario

Your e‑commerce platform must support multiple payment methods: **Credit Card**, **Debit Card**, and **Digital Wallet** (e.g., “PayNow”). Each method has different data requirements and processing logic, but the checkout flow should treat them **uniformly**.[^12][^3][^4]

### Learning goals

- **Abstraction + Inheritance**: define a common payment interface, implement per-provider logic.
- **Polymorphism**: call `process_payment()` without caring about the concrete class.
- **Encapsulation**: protect sensitive data (card numbers, wallet tokens).[^3][^4][^5]


### Requirements

1. Create an **abstract base class** `PaymentMethod` (use `abc.ABC`):
    - Abstract method: `process_payment(amount: float) -> bool`
    - Optional: `get_payment_info()` → returns a safe summary (no full card numbers).
2. Implement concrete classes:
    - `CreditCardPayment(PaymentMethod)`
        - Attributes: `_card_holder`, `_card_number_last4`, `_full_card_number` (private)
        - `process_payment()` → simulate success/failure (e.g., random or based on amount).
        - `get_payment_info()` → return something like `"Credit Card ****1234"`.
    - `DebitCardPayment(PaymentMethod)`
        - Similar to credit card but maybe different fees or rules.
    - `DigitalWalletPayment(PaymentMethod)`
        - Attributes: `_wallet_id`, `_token` (private)
        - `process_payment()` → simulate different behavior (e.g., instant success for small amounts).
        - `get_payment_info()` → return `"Digital Wallet (ID: abc123)"`.
3. Create an `Order` class:
    - Attributes: `order_id`, `amount`, `payment_method: PaymentMethod`
    - Method: `checkout()`:
        - Call `self.payment_method.process_payment(self.amount)`
        - Print a summary using `get_payment_info()`.
4. Demonstrate **polymorphism**:
    - Create several orders with different payment methods.
    - Call `order.checkout()` on each; the correct payment logic runs automatically.[^4][^3]

### Example usage

```python
card = CreditCardPayment("Ali", "1234567812345678")
wallet = DigitalWalletPayment("wallet_99", "tok_secret")

order1 = Order(101, 150.0, card)
order2 = Order(102, 40.0, wallet)

order1.checkout()
order2.checkout()
```


### Stretch goals

- Add a `RefundablePayment` mixin or base class that adds `refund(amount)` support for some methods.
- Add simple validation (e.g., card number length, wallet token format).
- Log payment attempts with timestamps using the `datetime` module.[^3][^4]


### Django mapping notes

- In Django, you might store payment metadata in models and delegate actual processing to services, but the **interface design** (one `process_payment()` method, multiple implementations) is the same idea.[^12][^3]

***

## Task 4 — Mini Django‑Style Model Inheritance (Design Exercise)

### Scenario

You are designing models for a blog + e‑commerce site. Several models share common fields (`created_at`, `updated_at`, `is_active`). You want to avoid repetition using **model inheritance**, similar to Django’s abstract base classes.[^7][^8][^6]

### Learning goals

- **Inheritance**: share common fields in a base class.
- **Encapsulation**: centralize timestamp logic.
- Understand how OOP maps to **Django model inheritance**.[^7][^6]


### Requirements (plain Python design first)

1. Create a base class `TimestampedModel`:
    - Attributes: `created_at`, `updated_at`, `is_active`
    - Method: `touch()` → updates `updated_at` to now (use `datetime`).
2. Create subclasses:
    - `Product(TimestampedModel)`
        - Extra: `name`, `price`, `stock`
    - `Order(TimestampedModel)`
        - Extra: `customer_name`, `total_amount`, `status`
    - `Article(TimestampedModel)`
        - Extra: `title`, `content`, `author_name`
3. Show how creating a `Product`, `Order`, or `Article` automatically gets `created_at`, `updated_at`, and `is_active` from the base class.
4. Discuss:
    - How would this look in Django? (Answer: `abstract = True` in `Meta`.)
    - Why is this useful? (DRY, consistent behavior, easier maintenance.)[^8][^6][^7]

### Stretch goals

- Add a `SoftDeleteMixin` that adds `deleted_at` and a `delete(soft=True)` method.
- Add a method `days_since_created()` using `datetime`.


### Django mapping notes

- Students can later implement this as:

```python
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
```

and then have `Product`, `Order`, `Article` inherit from `BaseModel`.[^8][^6][^7]

***

## Suggested Workflow for Your Students

1. **Pick one main task** (e.g., Task 1 or 2) and one smaller task (Task 4).
2. Implement in **plain Python** with clear class diagrams (even on paper).
3. Write a short explanation:
    - Where is **encapsulation** used?
    - Where is **inheritance** used?
    - Where is **polymorphism** used?
4. As a follow-up, sketch how the design would look in **Django models** (especially for Tasks 1, 2, and 4).[^9][^6][^7]

***

If you tell me your students’ level (beginner/intermediate) and how many hours they have, I can trim this into a **1–2 page handout** with just one or two tasks and sample starter code.[^1][^4][^3]
<span style="display:none">[^13][^14][^15]</span>

<div align="center">⁂</div>

[^1]: https://www.geeksforgeeks.org/system-design/object-oriented-programingoop-concepts-for-designing-sytems/

[^2]: https://www.linkedin.com/posts/rahulpodenla-podenla-_python-oop-backenddevelopment-activity-7368742568739704834-jTsV

[^3]: https://www.linkedin.com/posts/muhammad-fanik_i-recently-built-an-online-shopping-cart-activity-7434366105306984448-UzSZ

[^4]: https://www.linkedin.com/posts/ranjithsamudrala009_python-oop-objectorientedprogramming-activity-7374473203278237696-Ngqm

[^5]: https://prakash-sa.github.io/low-level-design-ultimatum/Introduction/OOP Principles.html

[^6]: https://www.linkedin.com/pulse/mastering-django-model-inheritance-simplified-pankaj-sharma-lyc7c

[^7]: https://blimto.com/learn/django/django-model-structure-options

[^8]: https://www.scribd.com/document/963021501/Full-Stack-Assignment

[^9]: https://www.youtube.com/watch?v=KphcFszdp8A

[^10]: https://medium.com/@skking5006j/creating-a-student-management-system-using-oop-a15f4ea3a197

[^11]: https://www.scribd.com/presentation/860223492/Abdella-Mohamed-Uu87768r

[^12]: https://medium.com/@whrtsewwandi/understanding-oop-with-real-life-examples-not-just-cars-and-animals-48364d6ec72a

[^13]: https://realpython.com/videos/guiding-principles-oop/

[^14]: https://www.youtube.com/watch?v=zcNInbjYnI4

[^15]: https://www.reddit.com/r/django/comments/1swbngk/models/

