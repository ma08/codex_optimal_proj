

import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


N, M = map(int, input().split())  # N:足場の数　M:経路の数
A = list(map(int, input().split()))  # 足場の距離

lcm_list = [A[0]]
for i in range(1, N):
    lcm_list.append(lcm(lcm_list[i-1], A[i]))


for i in range(M):
    L, R = map(int, input().split())
    if L == R:
        print(A[L-1])
        continue
    lcm_value = lcm_list[R-2] // lcm_list[L-1]
    print(lcm_value)
