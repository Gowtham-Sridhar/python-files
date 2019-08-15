
prompt = 'Welcome to PizzaHut | Make your order now'
prompt += '\nPlease add your favourite toppings for pizza'
prompt += '\n(Enter "quit" finish your order): '

order = True
# count = int(input('How many toppings you want? '))
while order:
    topping = input(prompt)

    # if topping == 'quit':
    #     order = False

    if topping == 'quit':
        break
    
    print('\tadding ' + topping + ' topping to your pizza.\n')
    # count = count - 1

print('Thank you for ordering pizza.')
