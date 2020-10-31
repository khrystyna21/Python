
name = 'Khrystyna'
day = 'Friday'
str = 'Good day {}! {} is a perfect day to learn some python'

print(f'Good day {name}! {day} is a perfect day to learn some python')

print(str.format(name, day))

print('Good day {1}! {0} is a perfect day to learn some python'.format(day, name))

print('Good day %s! %s is a perfect day to learn some python' % (name, day))


