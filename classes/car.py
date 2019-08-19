
class Car():
    ''' simple attempt to represent a car. '''

    def __init__(self, make, model, year):
        ''' initialize attributes to describe a car. '''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        ''' return neatly formatted descriptive name. '''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        ''' print a statement showing car mileage. '''
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')


my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())
my_car.odometer_reading = 23
my_car.read_odometer()