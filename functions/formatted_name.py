
def get_formatted_name(first_name, last_name, middle_name=''):
    ''' return fullname, neatly formatted. '''
    if middle_name:
        fullname = first_name + ' ' + middle_name + ' ' + last_name
    else:
        fullname = first_name + ' ' + last_name

    return fullname.title()

# person = get_formatted_name('gowtham', 'sridhar')
# print(get_formatted_name('hello', 'fm', '106.4'))
# print(person)

# this is infinite loop
while True:
    print('\nPlease enter your name')
    print('Enter "q" to close the program.')
    f_name = input('First Name: ')
    if f_name == 'q':
        break
    l_name = input('Last Name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('Hello, ' + formatted_name + '!')