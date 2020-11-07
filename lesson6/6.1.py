

str = input('Enter your string: ').lower()
words = str.split()
occurrences = dict()


for i in words:
    if i in occurrences:
        occurrences[i] += 1
    else:
        occurrences[i] = 1

print(occurrences)