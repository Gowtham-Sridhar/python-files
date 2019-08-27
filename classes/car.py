class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def fill_gas_tank(self):
        print('tank filled.')

    def get_descriptive_name(self):
        longname = str(self.year) + ' ' + self.make + ' ' + self.model
        print(longname.title())

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer_reading(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('access denied.')

    def increment_odometer_reading(self, mileage):
        if mileage > 0:
            self.odometer_reading += mileage
        else:
            print('access denied.')
    
class Battery:

    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def battery_upgrade(self):
        if self.battery_size != 85:
            self.battery_size = 85
        else:
            print('battery already upgraded.')
        

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        if self.battery_size == 75:
            miles = 240
        elif self.battery_size == 85:
            miles = 270

        message = 'This car go approx. ' + str(miles) + ' miles on full charge'
        print(message)
    
class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    # @override
    def fill_gas_tank(self):
        pass

car = ElectricCar('tesla', 's', 2019)
car.battery.describe_battery()
car.battery.get_range()

car.battery.battery_upgrade()
car.battery.describe_battery()
car.battery.get_range()

car.battery.battery_upgrade()
