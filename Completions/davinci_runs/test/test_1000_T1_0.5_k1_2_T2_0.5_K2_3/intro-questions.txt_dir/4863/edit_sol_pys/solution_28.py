

n = int(input())
s = 0
for i in range(1, n+1):
    ans = input()
    if ans == 'A' or ans == 'P' or ans == 'O' or ans == 'R':
        s += 1
print(s)
