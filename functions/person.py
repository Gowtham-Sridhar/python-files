
def build_person(firstname, lastname, age='', occupation=''):
    ''' Return a dictionary of information about a person '''
    person = {'first': firstname, 'last': lastname}
    if age:
        person['age'] = age
    if occupation:
        person['occupation'] = occupation
    return person

person = build_person('gowtham', 'sridhar')
person_1 = build_person('monesh', 'sridhar', age=19)
person_2 = build_person('sridhar', 'srinivasan', occupation='tailor')
person_3 = build_person('nalini', 'sridhar', occupation='chef', age=40)
print(person)
print(person_1)
print(person_2)
print(person_3)