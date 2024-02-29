# menu list
menu = ['Coffee', 'Burger', 'Pie', 'Chicken Sandwich', 'Chicken wrap']

# stock, has quantity for each menu item
stock = {'Coffee': 5, 'Burger': 4, 'Pie': 6,
         'Chicken Sandwich': 10, 'Chicken wrap': 10}

# price, has cost of each menu item
price = {'Coffee': 12.00, 'Burger': 6.99, 'Pie': 17.0,
         'Chicken Sandwich': 20.0, 'Chicken wrap': 11.0}

# total stock worth of cafe items
total_stock = 0.0


for item in menu:
    # current item quantity and cost
    quantity = stock[item]
    cost = price[item]
    # updating total stock with current item worth
    total_stock = total_stock + quantity * cost

print('Total stock worth of cafe items: ${:.2f}' .format(total_stock))