# 'There are 7.6 billion people in the world'
print('There are', 7.6, 'billion', 'people in the world')
print('There are' + ' ' + str(7.6) + ' ' + 'billion' + ' ' + 'people in the world')

# 'test@gmail.com'
print('test', 'gmail.com', sep='@')

# 'Beetroot is the best!!! May the borsch be with you.'
print('Beetroot is the best', end='!!! ')
print('May the borsch be with you.')

# 'Ocean names: Arctic, North Atlantic, South Atlantic, North Pacific, South Pacific, Indian, Southern Oceans'
print('Ocean names:', end=' ')
print('Arctic', 'North Atlantic', 'South Atlantic', 'North Pacific',
      'South Pacific', 'Indian, Southern', sep=', ', end=' ')
print('Oceans')

# 'My favorite movies:
# * "Inception"
# * "The Dark Knight"
# "Once Upon a Time in Hollywood"'

print('My favorite movies:', end='\n * ')
print('"Inception"', end='\n * ')
print('"The Dark Knight"', end='\n * ')
print('"Once Upon a Time in Hollywood"')
