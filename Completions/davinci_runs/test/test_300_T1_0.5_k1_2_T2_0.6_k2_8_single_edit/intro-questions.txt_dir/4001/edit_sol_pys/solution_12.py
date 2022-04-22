
def prime_factorization(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
 
N = int(input())  # N! を素因数分解する
pf = prime_factorization(N)  # pf は素因数分解の結果を格納するリスト
 
from collections import Counter
pf_count = Counter(pf)  # 素因数のカウント
 
ans = 0
for v in pf_count.values():
    # v=素因数の指数について、(1+v)//2 の累積和をとる
    ans += (1 + v) * v // 2
 
print(ans)
