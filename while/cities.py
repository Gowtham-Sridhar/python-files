
prompt = 'Please enter the name of city you have visited.'
prompt += '\n (Enter "quit" when you are finished): '

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print('I had love to go ' + city.title())