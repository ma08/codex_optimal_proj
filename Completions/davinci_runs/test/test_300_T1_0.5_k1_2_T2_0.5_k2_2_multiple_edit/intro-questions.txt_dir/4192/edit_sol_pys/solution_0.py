

n = int(input())
s = list(input())

for i in range(n):
    if s[i] == "R":
        print(n - i)
    elif s[i] == "L":
        print(i + 1)
        exit()
        exit()
