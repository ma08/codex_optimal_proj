from sys import stdin

N = int(stdin.readline())  # 1行目
S = stdin.readline()  # 2行目

x = 0
max_x = 0

for i in range(N):
    if S[i] == 'I':
        x += 1
    else:
        x -= 1
    if x > max_x:
        max_x = x

print(max_x)
