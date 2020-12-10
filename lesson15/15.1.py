import re


class Email:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    @staticmethod
    def validate(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(regex, email):
            raise ValueError('Invalid email')


# email = Email("khrystyna")
email1 = Email("khrystyna@gmail.com")
# print(email.email)
print(email1.email)
