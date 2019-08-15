
from pprint import pprint

users = {
    'gsridhar': {
        'first': 'gowtham',
        'last': 'sridhar',
        'location': 'thanjavur'
    },

    'msridhar': {
        'first': 'monesh',
        'last': 'sridhar',
        'location': 'trichy'
    }
}

for username, user_info in users.items():
    print('\nUsername: ' + username)
    fullname = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\tFullname: ' + fullname.title())
    print('\tLocation: ' + location.title())
