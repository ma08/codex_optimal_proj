
words = [input() for _ in range(int(input()))]

if words[0][0] != words[1][-1]:
    print("No")
    exit(0)

for i in range(1, len(words) - 1):
    if words[i][-1] != words[i + 1][0]:
        print("No")
        exit(0)

print("Yes")
