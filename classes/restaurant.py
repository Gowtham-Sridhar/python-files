
class Restaurant():
    ''' create restaurant model '''

    def __init__(self, name, type):
        ''' initialize restaurant name and cuisine type attributes. '''
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        ''' simulate describe about a restaurant. '''
        print('\nRestaurant name: ' + self.restaurant_name.title() + '.')
        print('Cuisine type: ' + self.cuisine_type + '.')

    def open_restaurant(self):
        ''' simulate indicatication about restaurant opened. '''
        print(self.restaurant_name.title() + ' now open.')


restaurant = Restaurant('Dawood Biriyani', 'Multi Cuisine')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

restaurant_1 = Restaurant('Sathyam', 'Single Cuisine')
restaurant_2 = Restaurant('Kannappa', 'Multi Cuisine')

restaurant.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()

restaurant_1.open_restaurant()