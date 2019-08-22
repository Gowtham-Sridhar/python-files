
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

    def update_odometer(self, mileage):
        ''' 
        set the odometer reading to given value. 
        reject the change if it attempt to change the odometer back.
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cannot rollback the odometer.')

    def increment_odometer(self, mileage):
        ''' add given amount to odometer reading. '''
        if mileage > 0:
            self.odometer_reading += mileage
        else:
            print('you cannot rollback the odometer.')
    
    def read_odometer(self):
        ''' print a statement showing car mileage. '''
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')


my_car = Car('audi', 'a4', 2016)
# my_car.odometer_reading = 30
print(my_car.get_descriptive_name())
my_car.update_odometer(40)
my_car.read_odometer()
my_car.update_odometer(10)
my_car.read_odometer()

print('\nincrement odometer by: 30')
my_car.increment_odometer(30)
# my_car.update_odometer(45)
my_car.read_odometer()
