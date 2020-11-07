

'''from random import shuffle

word=input('Write the word: ')
word_as_list = list(word)
ind = 0

while ind < 5:
    shuffle(word_as_list)
    print(''.join(word_as_list))
    ind +=1'''

import random

word = input('Enter your word: ')

str_to_generate = 5

while str_to_generate > 0:
    word_copy = word
    new_random_word = ''
    while True:
        random_char = random.choice(word_copy)
        new_random_word += random_char
        word_copy = word_copy.replace(random_char, '',1 )
        if not word_copy:
            print(new_random_word)
            break
    str_to_generate -= 1








