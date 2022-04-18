

# #Program starts here
# n, k = map(int, input().split())
# commands = input().split()

# egg = 0

# for i in range(len(commands)):
#     if "undo" in commands[i]:
#         for j in range(int(commands[i][5:])):
#             if i - j - 1 >= 0:
#                 egg -= int(commands[i-j-1])
#             elif i - j - 1 < 0:
#                 egg -= int(commands[0])
#     else:
#         egg += int(commands[i])

# print(egg % n)

# print(int(input()) % int(input()))

# print(8 % 4)

n, k = map(int, input().split())
egg = 0
for _ in range(k):
    c = input()
    if c == "undo":
        egg -= int(input())
    else:
        egg += int(c)

print(egg % n) 
