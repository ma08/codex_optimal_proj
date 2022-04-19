

n, m, k = map(int, input().split())

if k < n:
    print(k+1, 1)
elif k == n:
    print(n, 2)
else:
    k -= n
    m_ = m-1
    if k % m_ == 0:
        print(n-k//m_, m)
    else:
        print(n-k//m_, k % m_+1)


