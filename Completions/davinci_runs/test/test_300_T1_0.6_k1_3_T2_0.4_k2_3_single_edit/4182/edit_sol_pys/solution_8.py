import sys
input = sys.stdin.readline


n, m, x, y = map(int, input().split())  # n:x座標の数, m:y座標の数, x:x座標の最小値, y:y座標の最大値
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

for i in range(x+1, y+1):
    if all(x_list[j] < i for j in range(n)) and all(y_list[j] >= i for j in range(m)):  # x座標の最大値 < i < y座標の最小値
        print('No War')
        exit(0)
print('War')
