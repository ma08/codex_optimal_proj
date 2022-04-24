

# n = int(input())
# words = [input() for _ in range(n)]
words = [input() for _ in range(int(input()) - 1)]

# if words[0][0] != words[1][-1]:
#     print("No")
#     exit()

for i in range(len(words) - 1):
    if words[i][-1] != words[i + 1][0] or len(words[i]) != len(words[i + 1]):
        print("No")
        exit()

print("Yes")
