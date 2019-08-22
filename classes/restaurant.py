class Restaurant():
    ''' create restaurant model '''

    def __init__(self, name, type):
        ''' initialize restaurant name and cuisine type attributes. '''
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        ''' simulate describe about a restaurant. '''
        print('\nRestaurant name: ' + self.restaurant_name.title() + '.')
        print('Cuisine type: ' + self.cuisine_type + '.')

    def open_restaurant(self):
        ''' simulate indicatication about restaurant opened. '''
        print(self.restaurant_name.title() + ' now open.')

    def set_number_served(self, count):
        '''
        set the number served to given value. 
        reject the change if it attempt to rollback the number served.
        '''
        if count >= self.number_served:
            self.number_served = count
        else:
            print('you cannot rollback the number of served customers.')
        
    def increment_number_served(self, count):
        ''' add the given value to number served. '''
        if count > 0:
            self.number_served += count

    def served_customer(self):
        ''' display number of customers the restaurant has served. '''
        print('Number of customers served: ' + str(self.number_served))


restaurant = Restaurant('Dawood Biriyani', 'Multi Cuisine')
restaurant.set_number_served(53)
restaurant.increment_number_served(10)
restaurant.served_customer()

