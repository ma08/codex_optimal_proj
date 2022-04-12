
A, B = map(int, input().split())

def is_palindrome(num):
    num_str = str(num)
    is_palindrome_flag = True
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[len(num_str) - i - 1]:
            is_palindrome_flag = False
            break
    return is_palindrome_flag

count = 0
for i in range(A, B + 1):
    if is_palindrome(i):
        count += 1

print(count)
