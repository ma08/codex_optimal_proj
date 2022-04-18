def is_palindrom(input_str):
    for i in range(int(len(input_str) / 2)):
        if input_str[i] != input_str[-i - 1]:
            return False
    return True


input_str = input()
if is_palindrom(input_str):
    print('Yes')
else:
    print('No')
