from collections import Counter
orders = {
    "order_101": {"customer": "Alice", "items": ["Laptop", "Mouse"], "amount": 1200},
    "order_102": {"customer": "Bob", "items": ["Keyboard", "Phone"], "amount": 800},
    "order_103": {"customer": "Alice", "items": ["Phone"], "amount": 500},
    "order_104": {"customer": "Charlie", "items": ["Tablet", "Monitor"], "amount": 600},
}


# - Implement get_unique_customers(orders), which returns a set of unique customer names.
def get_unique_customers(orders):
    unique_customers = set()
    for x in orders.values():
        unique_customers.add(x["customer"])
    return unique_customers
#print(get_unique_customers(orders))

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
#print(get_total_spending_by_customer(orders))



# - Implement filter_orders_by_amount(orders, min_amount), which returns a list of order IDs where the total amount is greater than min_amount.

def filter_orders_by_amount(orders, min_amount):
    filtered_orders = []
    for order_id, x in orders.items():
        if x["amount"] > min_amount:
            filtered_orders.append(order_id)
    return filtered_orders
#print(filter_orders_by_amount(orders, 600))


# - Implement get_all_purchased_items(orders), which returns a set of unique items purchased across all orders.
def get_all_purchased_items(orders):
    unique_items = set()
    for x in orders.values():
        for item in x["items"]:
            if item not in unique_items:
             unique_items.add(item)
    return unique_items
#print(get_all_purchased_items(orders))
# - Implement order_generator(orders), which returns a generator yielding order details one at a time.


# Implement get_orders_by_customer(orders, customer_name), Returns a list of order IDs for a given customer.


#Implement get_most_expensive_order(orders) Returns the order ID of the most expensive order.

def get_most_expensive_orders(orders):
    expensive_order = ""
    print(orders.items())
    temp = 0

    for order_id, x in orders.items():
        print("this is in ", order_id, x)
        if x["amount"] >= temp: #if 1200 > 1200
            temp = x["amount"]
            expensive_order = order_id
    return expensive_order
# print(get_most_expensive_orders(orders))

#Implement get_least_expensive_order(orders) Returns the order ID of the least expensive order.

def get_least_expensive_order(orders):
    least_expensive = ""
    temp = float("inf")
    for order_id, x in orders.items():
        if x["amount"] < temp:  #1200 < 0 temp 
            temp = x["amount"]
            least_expensive = order_id
    return least_expensive
# print(get_least_expensive_order(orders))


#Implement get_items_purchased_by_customer(orders, customer_name) Returns a list of all items purchased by a given customer.
def get_items_purchased_by_customer(orders, customer_name):
    items_purchased = []
    for x in orders.values():
        if x["customer"] == customer_name:
            items_purchased.extend(x["items"])

    return items_purchased
#print(get_items_purchased_by_customer(orders, "Alice"))

#Implement get_most_frequent_customer(orders) Returns the name of the customer who placed the most orders.

def get_most_frequent_customer(orders):
    customer_count = {}

    for x in orders.values():
        customer = x["customer"]
        if customer in customer_count:
            customer_count[customer] += 1
        else:
            customer_count[customer] = 1
    # print(customer_count)

    max_orders = max(customer_count.values())
    # print(max_orders)
    most_frequent_customer = [x for x, count in customer_count.items() if count == max_orders]
    # print(most_frequent_customer)
            
print(get_most_frequent_customer(orders))

#Implement get_most_purchased_item(orders), Returns the item that appears most frequently in all orders.

def get_most_purchased_item(orders):
    item_count= {}
    for x in orders.values():
        items_purchased = x["items"] 
        for item in items_purchased:
            if items_purchased in item_count:
                item_count[items_purchased] = 1
        # item_count.update(items_purchased)
    print(item_count)

    most_purchased_item = max(item_count, key=item_count.get)
    return most_purchased_item

print(get_most_purchased_item(orders))
