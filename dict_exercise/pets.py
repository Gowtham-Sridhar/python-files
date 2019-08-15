
tiger = {
    'type': 'dog',
    'owner': 'balaji'
}

chinchu = {
    'type': 'cat',
    'owner': 'reshma'
}

jigli = {
    'type': 'parrot',
    'owner': 'sangeetha'
}

pets = [tiger, chinchu, jigli]
# print(pets)

for pet in pets:

    for key, value in pet.items():
        print('\n' + key + ' : ' + value)