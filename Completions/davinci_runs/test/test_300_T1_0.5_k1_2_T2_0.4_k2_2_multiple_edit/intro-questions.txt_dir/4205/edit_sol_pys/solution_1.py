

n = int(input())
p = list(map(int, input().split()))

# 配列をソートする
sorted_p = sorted(p)

# 順番に比較して、隣り合う数字が違うなら、その数字が何番目にあるかを記録する
for i in range(n):
    if p[i] != sorted_p[i]:
        if p[i] == sorted_p[i+1]:
            p[i], p[i+1] = p[i+1], p[i]
        else:
            print('NO')
            exit()

print('YES')
