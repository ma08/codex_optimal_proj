# 解答
# N: 整数の個数
# A_i: i番目の整数
N = int(input())
A = list(map(int, input().split()))


# 入力された整数を辞書に登録
# key: 整数の値
# value: 整数の個数
d = {}
for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

# 辞書の値が奇数のものを数える
cnt = 0
for v in d.values():
    if v % 2 == 1:
        cnt += 1

print(cnt)
