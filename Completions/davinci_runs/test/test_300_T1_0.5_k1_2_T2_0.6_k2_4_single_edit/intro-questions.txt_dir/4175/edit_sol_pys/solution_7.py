
N = int(input())

words = []
words = [input() for _ in range(N)]

for i in range(1, N):
    if words[i] in words[:i] or words[i][0] != words[i - 1][-1]:
        print("No")
        exit()

print("Yes")
