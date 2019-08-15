
def print_models(unprinted_designs, completed_models):
    '''
    simulate printing each design, until none are left.
    move each design to completed models after printing.
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    ''' show all the models that are printed. '''
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print('\n --- after task --- ')
print('Original list: {}'.format(unprinted_designs))
print(completed_models)