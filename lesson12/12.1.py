
def animal_talk(animal):
    print(animal.talk())

class Animal:

    def talk():
        pass

class Cat(Animal):
    def talk(self):
        return 'Meow'

class Dog(Animal):
    def talk(self):
        return 'Woof Woof'

cat = Cat()
dog = Dog()

print(cat.talk())
print(dog.talk())

animal_talk(cat)
animal_talk(dog)
