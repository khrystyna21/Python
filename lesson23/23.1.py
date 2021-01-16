# # Task 1
#
# def to_power(x, exp):
#     if exp == 1:
#         return x
#     if exp < 0:
#         raise ValueError ('This function works only with exp > 0')
#     return (x * to_power(x, exp-1))
#
# print(to_power(2, 3))
# print(to_power(3.5, 2))
# # print(to_power(2, -1))



# Task 2

# from typing import Optional
# def is_palindrome(looking_str: str, index: int = 0) -> bool:
#     if len(looking_str) < 1:
#         return True
#     else:
#         if looking_str[0] == looking_str[-1]:
#             return is_palindrome(looking_str[1:-1])
#         else:
#             return False
#
#
# print(is_palindrome('mom'))
# print(is_palindrome('sassas'))
# print(is_palindrome('o'))


# #Task 3
#
# from typing import Optional
# def mult(a: int, n: int) -> int:
#     if n == 0 or a == 0:
#         return 0
#     if a < 0 or n < 0:
#         raise ValueError("This function works only with postive integers")
#     else:
#         return (a + mult(a, n-1))
#
#
# print(mult(2, 4))


#Task 4
#
# def reverse(input_str: str) -> str:
#     if len(input_str) == 1:
#         return input_str
#     return input_str[-1] + reverse(input_str[:-1])
#
#
# print(reverse("hello"))
# print(reverse("o"))


# Task 5

def sum_of_digits(digit_string: str) -> int:
    try:
       if int(digit_string) == 0:
           return 0
       return int(digit_string) % 10 + sum_of_digits(int(digit_string) / 10)
    except ValueError:
        print("input string must be digit string")


print(sum_of_digits('12345'))
# print(sum_of_digits('test'))



