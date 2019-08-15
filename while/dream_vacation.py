
title = 'Dream Vacation Poll | Enjoy'
prompt = 'If you could visit one place in the world, where would you go? '

response = {}
polling_active = True

print(title)
while polling_active:
    name = input('What is your name? ')
    vacation = input(prompt)

    response[name] = vacation

    repeat = input('\nLet another person take poll? ')
    if repeat == 'no':
        polling_active = False

for name, vacation in response.items():
    print(name.title() + ' like to go ' + vacation)

