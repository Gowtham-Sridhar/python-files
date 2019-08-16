
def print_models(unprinted_designs, completed_models):
    '''
    simulate printing each design, until none are left.
    move each design to completed models after printing.
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)
        completed_models.append(current_design)
