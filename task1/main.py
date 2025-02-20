orders = {
    "order_101": {"customer": "Alice", "items": ["Laptop", "Mouse"], "amount": 1200},
    "order_102": {"customer": "Bob", "items": ["Keyboard", "Phone"], "amount": 800},
    "order_103": {"customer": "Alice", "items": ["Phone"], "amount": 900},
    "order_104": {"customer": "Charlie", "items": ["Tablet", "Monitor"], "amount": 600},
}


# - Implement get_unique_customers(orders), which returns a set of unique customer names.
def get_unique_customers(orders):
    unique_customers = set()
    for x in orders.values():
        unique_customers.add(x["customer"])
    return unique_customers
print(get_unique_customers(orders))

# - Implement get_total_spending_by_customer(orders), which returns a dictionary where keys are customer names and values are their total spending.
def get_total_spending_by_customer(orders):
    total_spent = {}
    for x in orders.values():
       customer = x["customer"]
       spending = x["amount"]
       if customer in total_spent.keys():
           total_spent.update({customer : spending + total_spent[customer]})
       else:
           total_spent[customer] = spending
    return total_spent
print(get_total_spending_by_customer(orders))



# - Implement filter_orders_by_amount(orders, min_amount), which returns a list of order IDs where the total amount is greater than min_amount.

def filter_orders_by_amount(orders, min_amount):
    filtered_orders = []
    for order_id, x in orders.items():
        if x["amount"] > min_amount:
            filtered_orders.append(order_id)
    return filtered_orders
print(filter_orders_by_amount(orders, 600))


# - Implement get_all_purchased_items(orders), which returns a set of unique items purchased across all orders.
def get_all_purchased_items(orders):
    unique_items = set()
    for x in orders.values():
        for item in x["items"]:
            if item not in unique_items:
             unique_items.add(item)
    return unique_items
print(get_all_purchased_items(orders))
# - Implement order_generator(orders), which returns a generator yielding order details one at a time.
