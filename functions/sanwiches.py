
# exercise 8-12
def make_sandwich(*fillings):
    ''' summarize the sandwich we about to make. '''
    print('\nMaking Sandwich with following fillings.')
    for filling in fillings:
        print('- ' + filling)

make_sandwich('pepperoni')
make_sandwich('cheese', 'chicken')
make_sandwich() 
    