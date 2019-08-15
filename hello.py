 
prompt = 'Which party you like to vote?'
prompt += '\nADMK | DMK | NTK | PMK | BJP'
prompt += '\nYour choice: '

response = {}

polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    party = input(prompt)

    response[name] = party
    repeat = input('\nLet another person response: ')
    if repeat == 'no':
        polling_active = False

result_list = []
print('\n --- Polling Result ---')
for name, party in response.items():
    result_list.append(party)
    print(name.title() + ' like to vote ' + party.upper())

result = '\nADMK votes: ' + str(result_list.count('admk'))
result += '\nDMK votes: ' + str(result_list.count('dmk'))
result += '\nNTK votes: ' + str(result_list.count('ntk'))
result += '\nPMK votes: ' + str(result_list.count('pmk'))
result += '\nBJP votes: ' + str(result_list.count('bjp'))

print(result)
