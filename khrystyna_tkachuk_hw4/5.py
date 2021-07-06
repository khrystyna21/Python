# task 5

def count_letters(word):
    word = word.lower()
    list_of_letters = list(word)
    occurrences = dict()

    for i in list_of_letters:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1
    return occurrences


print(count_letters('stringsample'))


