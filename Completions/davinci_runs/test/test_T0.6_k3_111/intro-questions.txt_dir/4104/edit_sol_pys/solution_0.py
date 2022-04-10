#
# exp = input()
#
# # Convert to list of numbers and list of operators
# nums = []
# op = []
#
# n = ''
# for c in exp:
#     if c.isdigit():
#         n += c
#     else:
#         nums.append(int(n))
#         op.append(c)
#         n = ''
# nums.append(int(n))
#
# # Evaluate expression using order of operations
# total = nums[0]
# for i in range(len(op)):
#     if op[i] == '+':
#         total += nums[i+1]
#     elif op[i] == '-':
#         total -= nums[i+1]
#
# print(total)


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_palindrome(s):
    return s == s[::-1]


def is_palindrome_prime(n):
    return is_prime(n) and is_palindrome(str(n))


def main():
    for i in range(100, 1001):
        if is_palindrome_prime(i):
            print(i)


main()
