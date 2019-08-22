class User():
    ''' creating user model '''

    def __init__(self, firstname, lastname, age, gender, email, country):
        ''' initialize attributes for user '''
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.email = email
        self.country = country
        self.login_attempt = 0

    def describe_user(self):
        ''' describe user detail summery. '''
        summary = 'firstname: ' + self.firstname.title()
        summary += '\nlastname: ' + self.lastname.title()
        summary += '\nage: ' + str(self.age)
        summary += '\ngender: ' + self.gender.title()
        summary += '\nemail: ' + self.email
        summary += '\ncountry: ' + self.country.title()
        print(summary)
    
    def greetings(self):
        ''' Display personalized greetings for user. '''
        fullname = self.firstname + ' ' + self.lastname
        print('\nHello, ' + fullname)

    def increment_login_attempt(self):
        ''' increment login attempt value by 1. '''
        self.login_attempt += 1
    
    def reset_login_attempt(self):
        ''' set login attempt value to 0. '''
        self.login_attempt = 0
    
    def get_login_attempts_count(self):
        ''' display number of login attempts. '''
        print('login attempts: ' + str(self.login_attempt))
    

user = User('Gowtham', 'Sridhar', 22, 'male', 'gowtham@email.com', 'india')
# user.describe_user()
# user.greetings()

testuser = User('test', 'user', 12, 'female', 'test@email.com', 'australia')
testuser.increment_login_attempt()
testuser.get_login_attempts_count()
testuser.reset_login_attempt()
testuser.get_login_attempts_count()

