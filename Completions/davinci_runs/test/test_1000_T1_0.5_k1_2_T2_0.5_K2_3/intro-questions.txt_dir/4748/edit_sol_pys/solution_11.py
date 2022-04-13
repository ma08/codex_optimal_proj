

h, n, m = map(int, input().split())  # 세로, 가로, 가로

a = 0  # 세로
b = 0  # 가로

for i in range(1, h + 1):
    a += (2 * i - 1)
    b += (2 * i)

if a <= n: #너비가 n보다 작을 경우
    print(0, m)
else: #너비가 n보다 클 경우
    a -= n
    if a <= m*2: #너비가 두배의 가로 크기보다 작을 경우
        print(a//2, m - (a//2))
    else: #너비가 두배의 가로 크기보다 클 경우
        print(m, 0)
