# 何個入っているか、何個入れられるか、何分かかるか
n, x, t = map(int, input().split())

if n % x == 0:
    print(t * (n // x))
else:
    print(t * (n // x + 1))
