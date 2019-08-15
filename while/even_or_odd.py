
number = input('Enter a number, I will tell you if it is Odd or Even?: ')
number = int(number)

if number % 2 == 0:
    print('The number ' + str(number) + ' is Even.')
else:
    print('The number ' + str(number) + ' is Odd.')
