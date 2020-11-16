


'''str = "Hello file world!"

with open('myfile.txt', 'w') as file_object:
    file_object.write(str)'''

with open('myfile.txt', 'r') as file_object:
    str = file_object.read()

print(str)
