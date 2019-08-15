
from pprint import pprint

person_1 = {
    'name': 'gowtham',
    'college': 'kumaraguru college of technology',
    'education': 'bachelor of engineering',
    'location': 'thanjavur'
}

person_2 = {
    'name': 'monesh',
    'college': 'saranathan college of engineering',
    'education': 'bachelor of technology',
    'location': 'trichy'
}

people = []

people.append(person_1)
people.append(person_2)

for user_info in people:

    for key, value in user_info.items():
        print('\n' + key.title() + ' : ' + value.title())