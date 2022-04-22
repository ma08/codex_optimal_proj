N = int(input())
r = int(math.ceil(math.sqrt(N)))
for i in range(r, 0, -1):  # 後ろから順に割り切れる数を探す
    if N % i == 0:
        print(N // i // 10 ** (len(str(i)) - 1))
        break
