
sandwich_orders = ['pastrami', 'cheese', 'tuna', 'pastrami', 'sausage', 'egg', 'veg', 'pastrami']
finished_sandwiches = []

print('\nrestaurant has run out of pastrami')
sandwich = 'pastrami'
while sandwich in sandwich_orders:
    sandwich_orders.remove(sandwich) 

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your ' + sandwich + ' sandwich.')
    order = sandwich + ' sandwich'
    finished_sandwiches.append(order)

print('\n--- order list ---')
for sandwich in finished_sandwiches:
    print('\t' + sandwich.title())