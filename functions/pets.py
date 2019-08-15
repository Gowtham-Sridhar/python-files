
def describe_pet(pet_name, animal_type='dog'):
    ''' Display the pet information '''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + ' name is ' + pet_name)

# describe_pet('hamster', 'harry')
# keyword arguments
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet('willie')
# describe_pet()