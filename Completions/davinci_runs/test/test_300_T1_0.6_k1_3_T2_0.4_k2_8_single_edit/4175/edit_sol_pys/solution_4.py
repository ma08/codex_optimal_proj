

# n = int(input())
# words = [input() for _ in range(n)]
words = [input() for _ in range(int(input()))]
# words = ["test", "test", "test"]
if words[0][0] != words[1][-1]:
    print("No")
    exit()

for i in range(1, len(words) - 1):
    if words[i][-1] != words[i + 1][0]:
        print("No")
        exit()

print("Yes")
