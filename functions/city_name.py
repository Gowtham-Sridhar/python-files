
def city_country(city, country):
    ''' return a information about a city '''
    info = city + ', ' + country
    return info.title()

info_0 = city_country('santiago', 'chile')
print(info_0)
info_1 = city_country('thanjavur', 'india')
print(info_1)
info_2 = city_country('sydney', 'australia')
# print(info_2 + '\n' + info_1)