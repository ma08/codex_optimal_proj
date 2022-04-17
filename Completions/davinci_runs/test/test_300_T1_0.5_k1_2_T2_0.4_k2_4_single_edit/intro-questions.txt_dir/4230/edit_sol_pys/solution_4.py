

x = int(input()) # 현재 위치
n = int(input()) # 보관함의 개수
p = list(map(int, input().split())) # 보관함의 위치

p.sort()

if x < p[0]:
    print(p[0] - x)
elif x > p[n-1]:
    print(x - p[n-1])
else:
    for i in range(1, n):
        if p[i-1] < x and x < p[i]:
            if abs(p[i-1] - x) < abs(p[i] - x):
                print(p[i-1] - x)
            else:
                print(p[i] - x)
            break
