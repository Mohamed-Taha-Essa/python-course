
"""1. Calculates and prints the total revenue across all orders.
2. Prints how many orders exist for each status.
3. Finds and prints the customer with the highest single order total.
4. Prints a list of all unique items ordered across every order (no duplicates — a `set` may help here)."""
orders = [
    {"id": 1, "customer": "Ali", "items": ["shoes", "hat"], "total": 75.98, "status": "delivered"},
    {"id": 2, "customer": "Sara", "items": ["laptop"], "total": 899.99, "status": "shipped"},
    {"id": 3, "customer": "Mo", "items": ["mouse", "keyboard", "monitor"], "total": 220.00, "status": "pending"},
    {"id": 4, "customer": "Lina", "items": ["phone case"], "total": 15.99, "status": "delivered"},
]