
cities = {
    'thanjavur': {
        'country': 'india',
        'population': 350000,
        'fact': 'thanjavur is the peaceful place.'
    },

    'trichy': {
        'country': 'india',
        'population': 550000,
        'fact': 'india-s largest gun power manufacturar.'
    },

    'monaco': {
        'country': 'italy',
        'population': 60000,
        'fact': 'beautiful city in the world.'
    }
}

for city, city_info in cities.items():
    print('\nCity: ' + city.title())
    for key, value in city_info.items():
        print('\t' + key.title() + ' : ' + str(value).title())