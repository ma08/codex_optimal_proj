

# from collections import Counter
# n = int(input())  # input is number of rows
# c = Counter([input().split()[1] for _ in range(n)])  # split() split the string by space, and return a list of strings.
# print(c['soft']*c['hard'])  # c is a dict, c['soft'] is the number of soft

# n = int(input())
# soft, hard = 0, 0
# for _ in range(n):
#     name, type = input().split()  # split() split the string by space, and return a list of strings.
#     if type == 'soft':
#         soft += 1
#     elif type == 'hard':
#         hard += 1
# print(soft*hard)

n = int(input())
soft, hard = 0, 0
for _ in range(n):
    name, type = input().split()
    if type == 'soft':
        soft += 1
    elif type == 'hard':
        hard += 1
print(soft*hard)
