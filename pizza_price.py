#!/usr/bin/env python3

if __name__ == '__main__':

    print("==========================")
    app = "BPP Pizza Price Calculator"
    x = app.title()
    print(x)
    print("==========================")
    x = input("Press enter to start your order.")
print()
pizza_price = 12.0
pizza_count = float(input("How many pizzas? "))
if pizza_count <= 0:
    print('Error: Order must contain 1 or more pizzas.')
delivery_cost = 2.5 if pizza_count <= 5 else 0.0
collection_cost = 0.0
total_pizza_cost = pizza_price * pizza_count
day = (input("What day is it? "))
rest = "Monday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
discount = "Tuesday"
if day == "Tuesday":
    total_pizza_cost *= 0.5
    print("50% discount applied")
else:
    print("50% discount not applied")
app_order = (input("Did you use the app? (Yes/No) "))
if app_order == "Yes":
    total_pizza_cost *= 0.75
    print("25% discount applied")
else:
    print("25% discount not applied")
service = (input("Delivery or Collection? (Delivery/Collection) "))
if service == "Collection":
    order_total = total_pizza_cost
    print("Free collection applied")
else:
    order_total = total_pizza_cost + delivery_cost
    print("£2.50 charge added for delivery")
order_total = total_pizza_cost + (delivery_cost if service == "Delivery" else collection_cost)
print(f'Total Pizza Cost: £{total_pizza_cost:.2f}')
if service == "Delivery":
    print(f'Delivery Cost: £{delivery_cost:.2f}')
else:
    print(f'Collection Cost: £{collection_cost:.2f}')
if day == "Tuesday" and app_order == "Yes":
    print("50% discount applied for Tuesday and 25% discount for the app.")
    print(f'Amount to charge: £{order_total:.2f}')
else:
    print(f'Amount to charge: £{order_total:.2f}')
