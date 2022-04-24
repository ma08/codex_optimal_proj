

n = int(input()) + 1
s = list(input())[:n]

for i in range(n - 1):
    if s[i] == "R":
        print(n - i - 1)
        exit()
