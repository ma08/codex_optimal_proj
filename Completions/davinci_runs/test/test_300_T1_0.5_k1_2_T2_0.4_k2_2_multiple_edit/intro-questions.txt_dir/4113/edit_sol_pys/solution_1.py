
# 入力
N = int(input())

# 4で割り切れるかどうか
for i in range(N//4+1):
    # 7で割り切れるかどうか
    for j in range(N//7+1):
        # 4と7で割り切れるかどうか
        if N == i*4 + j*7:
            print("Yes")
            exit()
print("No")
