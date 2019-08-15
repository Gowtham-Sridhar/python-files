
prompt = 'Welcome to Cinema | Book your tickets'
prompt += '\nTicket counter'
prompt += '\nPlease enter your age: '

# range = int(input('How many tickets: '))
active = True
while active:
    age = input(prompt)

    # if age == 'quit':
    #     break

    if age == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
            ticket_cost = 0
        elif 3 <= age <= 12:
            ticket_cost = 10
        elif age > 12:
            ticket_cost = 15

        if ticket_cost == 0:
            print('\nFree Ticket\n')
        else:
            print('\nYour ticket cost is $' + str(ticket_cost) + '.\n')
    
    # range = range - 1