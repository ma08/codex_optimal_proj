x, k, d = map(int,input().split())

if k*d > abs(x):
    k = abs(x) // d  # 何回dで割れるか
    x -= k*d  # 割れる回数だけdを引く
    if abs(x) % d == 0:
        print(abs(x))
    else:
        print(abs(x) - d)
else:
    print(abs(x - k*d))
