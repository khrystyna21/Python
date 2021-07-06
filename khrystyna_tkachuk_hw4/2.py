# task 2

def is_palindrome(looking_str):
    looking_str = looking_str.lower()
    if len(looking_str) < 1:
        return True
    else:
        if looking_str[0] == looking_str[-1]:
            return is_palindrome(looking_str[1:-1])
        else:
            return False


print(is_palindrome('cat'))
print(is_palindrome('Anna'))
print(is_palindrome('o'))
