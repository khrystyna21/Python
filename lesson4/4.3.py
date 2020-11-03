

from random import shuffle

word=input('Write the word: ')
word_as_list = list(word)
ind = 0

while ind < 5:
    shuffle(word_as_list)
    print(''.join(word_as_list))
    ind +=1








