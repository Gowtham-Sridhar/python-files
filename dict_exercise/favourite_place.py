
favorite_place = {
    'gowtham': ['thanjavur', 'coimbatore', 'kerala'],
    'monesh': ['trichy', 'madurai', 'tirunelveli'],
    'nandhu': ['singapore', 'paris', 'kerala']
}

for name, places in favorite_place.items():
    print('\n' + name + ' favourite places are: ')
    for place in places:
        print('\t' + place)