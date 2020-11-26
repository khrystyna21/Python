


class Person():

    def __init__(self, firstname, lastname, age, weight, height):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.weight = weight
        self.height = height

    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old')

    def weight_change(self, number_kg):
        self.weight += number_kg

    def grow_up(self, number_cm):
        self.height += number_cm

    def get_older(self, number_year):
        self.age += number_year

class Student(Person):

    def __init__(self, firstname, lastname, age, weight, height, class_year, avg_mark):
        super().__init__(firstname, lastname, age, weight, height)
        self.class_year = class_year
        self.avg_mark = avg_mark

    def next_class(self):
        if self.class_year <= 11:
            self.class_year += 1
        else:
            return 'End of school'

    def mark(self, test):
        if test in range(1, 13):
            self.avg_mark = (self.avg_mark + test) / 2

class Teacher(Person):
    def __init__(self, firstname, lastname, age, weight, height, salary, year_experience):
        super().__init__(firstname, lastname, age, weight, height)
        self.salary = salary
        self.year_experience = year_experience

    def salary_raise(self, raise_number):
        self.salary += raise_number

    def gain_experience(self):
        self.year_experience += 1

person = Person('Khrystyna', 'Tkachuk', 24, 54, 165)

person.talk()
person.weight_change(2)
person.grow_up(5)
person.get_older(2)
print(person.weight)
print(person.height)
print(person.age)

student = Student('Anna', 'Frank', 12, 40, 150, 6, 9.1)

student.next_class()
print(student.class_year)
student.mark(12)
print(student.avg_mark)

teacher = Teacher('Jon', 'Snow', 33, 77, 173, 5500, 3)

teacher.salary_raise(500)
print(teacher.salary)
teacher.gain_experience()
print(teacher.year_experience)