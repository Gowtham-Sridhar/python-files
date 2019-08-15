
def build_car(manufacturer, model, **car_info):
    ''' build a dictionary containing everything we know about car '''
    cars = {}
    cars['manufacurer'] = manufacturer
    cars['model'] = model

    for key, value in car_info.items():
        cars[key] = value

    return cars

cars = build_car('subaru', 'outback', color='blue', tow_package=True)
print(cars)