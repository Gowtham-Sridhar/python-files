
def greet_user(names):
    ''' Display simple greetings to each user in the list. '''
    for name in names:
        print('Hello, ' + name.title() + '!')

usernames = ['gowtham', 'sridhar', 'monesh', 'nalini']
greet_user(usernames)
