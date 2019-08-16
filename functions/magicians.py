
def show_magicians(names):
    ''' Display the name of each magician in the list. '''
    for name in names:
        print('\t' + name)


def make_great(magicians):
    ''' adding phrash "great" to each magician name '''
    great_magicians = []
    for magician in magicians:
        great_magician = 'Great ' + magician
        great_magicians.append(great_magician)
    
    return great_magicians


magicians = ['David Copperfield', 'Harry Houdini', 'Penn and Teller', 'Criss Angel', 'David Blaine']
great_magicians = make_great(magicians[:])

# print the name of magicians
show_magicians(magicians)
# print great magicians
print('\n--- Great Magicians ---')
show_magicians(great_magicians)
