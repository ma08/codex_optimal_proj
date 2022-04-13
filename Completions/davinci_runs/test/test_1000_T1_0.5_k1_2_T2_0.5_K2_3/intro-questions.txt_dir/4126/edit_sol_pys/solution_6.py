
input_str = input()

is_palindrom = True
for i in range(int(len(input_str) / 2)):
    if input_str[i] != input_str[-i - 1]:
        is_palindrom = False

if is_palindrom:
    print('Yes')
else:
    print('No')
