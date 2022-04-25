# coding=utf-8
input_str = input()

if len(input_str) == 1:
    is_palindrome = True
elif len(input_str) == 2:
    if input_str[0] == input_str[1]:
        is_palindrome = True
    else:
        is_palindrome = False
else:
    is_palindrome = True
    for i in range(int(len(input_str) / 2)):
        if input_str[i] != input_str[-i - 1]:
            is_palindrome = False

if is_palindrome:
    print('Yes')
else:
    print('No')
