
favourite_number = {
    'gowtham': [6, 9, 3],
    'nandhu': [4, 30],
    'sridhar': [26],
    'nalini': []
}

for name, numbers in favourite_number.items():
    print('\n' + name + ' favourite numbers are:')
    
    if len(numbers) > 1:
        for num in numbers:
            print('\t' + str(num))
    elif len(numbers) == 0:
        print('\t' + 'no data found.')
    else:
        print('\t' + str(numbers.pop()))
