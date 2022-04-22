

n, x, y = map(int, input().split())
n = list(input())  # 入力した文字をリストに変換

if n[y] == '0':
    n[y] = '1'
else:
    n[y] = '0'
    for i in range(y+1, x):
        if n[i] == '0':
            n[i] = '1'
            break
        else:
            n[i] = '0'

print(n.count('0'))
