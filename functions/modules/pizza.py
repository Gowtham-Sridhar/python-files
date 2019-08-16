
def make_pizza(size, *toppings):
    ''' summarize the pizza we about to make. '''
    print('\nMaking a ' + str(size) + '-inch pizza with following toppings.')
    for topping in toppings:
        print('- ' + topping)
