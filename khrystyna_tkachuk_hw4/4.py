# task 4

import string


def common_symbol(strings):
    sets = [set(word) for word in strings]
    return sets[0].intersection(*sets[1:])


def one_appearance(strings):
    sets = [set(word) for word in strings]
    return sets[0].union(*sets[1:])


def two_appearance(strings):
    sets = [set(word) for word in strings]
    result = set()
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            result.update(sets[i].intersection(sets[j]))
    return result


def not_used(strings):
    sets = [set(word) for word in strings]
    set_ancii = set(string.ascii_lowercase)
    return set_ancii.difference(sets[0].union(*sets[1:]))


strings = ["hello", "world", "python"]


print(common_symbol(strings))
print(one_appearance(strings))
print(two_appearance(strings))
print(not_used(strings))






