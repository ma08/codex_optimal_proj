import sys



n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for i in range(n)]

if len(words) != len(set(words)):
    print("No")
    sys.exit()

for i in range(1, n):
    if words[i-1][-1] != words[i][0]:
        print("No")
        sys.exit()

print("Yes")
