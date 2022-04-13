

K, S = map(int, input().split())

count = 0

for x in range(K+1):  # ループ処理で全探索
    for y in range(K+1):
        for z in range(K+1):
            if x + y + z == S:
                count += 1



# 別解
# 全探索ではなく、組み合わせを用いて解く

K, S = map(int, input().split())

count = 0

for x in range(K+1):
    for y in range(K+1):
        z = S - x - y
        if z >= 0 and z <= K:
            count += 1

print(count)
print(count)
