
class Dog():
    ''' A simple attempt to model a dog '''
    def __init__(self, name, age):
        ''' initialize name and age attributes '''
        self.name = name
        self.age = age

    def sit(self):
        ''' simulate a dog sitting in respond to command. '''
        print(self.name.title() + ' is now sitting.')
    
    def rollover(self):
        ''' simulate rollover in respond to command. '''
        print(self.name.title() + ' rolled over!')
    
dog = Dog('kelly', 3)
print(dog.age)
