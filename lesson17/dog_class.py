class Dog():


    def __init__(self, name, dog_age):
        self.name = name
        self.dog_age = dog_age
        self.age_factor = 7

    def human_age(self):
        return (self.dog_age * self.age_factor)


