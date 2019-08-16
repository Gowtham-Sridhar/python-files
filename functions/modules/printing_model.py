
from print_model import print_models

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