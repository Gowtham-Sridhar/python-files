
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
    

user = User('Gowtham', 'Sridhar', 22, 'male', 'gowtham@email.com', 'india')
user.firstname = 'monesh'
print(user.firstname)
user.describe_user()
user.greetings()

# test_user = User('monesh', 'sridhar')