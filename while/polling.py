
response = {}

polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    color = input('Which color you like? ')

    response[name] = color

    repeat = input('\nYou want to continue? ')
    if repeat == 'no':
        polling_active = False

print('\n --- Polling Result ---')
for name, color in response.items():
    print(name.title() + ' likes ' + color.title())