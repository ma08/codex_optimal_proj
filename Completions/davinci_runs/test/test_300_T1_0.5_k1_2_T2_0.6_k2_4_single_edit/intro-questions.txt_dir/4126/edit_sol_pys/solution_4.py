


input_str = input()

is_palindrome = True
for i in range(int(len(input_str) / 2)):
    if input_str[i] != input_str[-i - 1]:
        is_palindrome = False

if is_palindrome:
    print('Yes')
else:


    print('No')
