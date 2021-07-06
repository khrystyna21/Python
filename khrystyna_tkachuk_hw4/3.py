# task 3

def get_shortest_word(str):
    word = ""
    word_list = []
    str = str + " "
    for letter in range(len(str)):
        if str[letter] != ' ':
            word = word + str[letter]
        else:
            word_list.append(word)
            word = ""

    small = word_list[0]

    for wrd in range(len(word_list)):
        if len(small) > len(word_list[wrd]):
            small = word_list[wrd];
    return small

print(get_shortest_word('Python is simple and effective!'))
print(get_shortest_word('Any pythonista like namespaces a lot, a? O'))

