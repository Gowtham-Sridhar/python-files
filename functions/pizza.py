
def make_pizza(size, *toppings):
    ''' summarize the pizza we about to make. '''
    print('\nMaking a ' + str(size) + '-inch pizza with following toppings.')
    for topping in toppings:
        print('- ' + topping)

make_pizza(12, 'pepperoni')
make_pizza(18, 'cheese', 'green chilli', 'chicken')
make_pizza(16, 'pepperoni', 'cheese')