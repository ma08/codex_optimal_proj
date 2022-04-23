
input_str = input('Enter string: ')


def is_palindrome(input_str):
    is_palindrome = True
    for i in range(int(len(input_str) / 2)):
        if input_str[i] != input_str[-i - 1]:
            is_palindrome = False
    return is_palindrome


print(is_palindrome(input_str))
