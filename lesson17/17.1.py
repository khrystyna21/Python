
import unittest
import decorator_example
import dog_class


class DecoratorTestCase(unittest.TestCase):

    def test_decorator(self):
        slogan = decorator_example.create_slogan('Steve')
        self.assertEqual(slogan, 'Steve drinks * in his brand new *!')



class DogTestCase(unittest.TestCase):

    def setUp(self):
        self.my_dog = dog_class.Dog('Jack', 1)

    def test_human_age(self):
        self.assertEqual(self.my_dog.dog_age, 1)
        self.assertEqual(self.my_dog.human_age(), 7)
        self.my_dog.dog_age = 2
        self.assertEqual(self.my_dog.human_age(), 14)

unittest.main()
