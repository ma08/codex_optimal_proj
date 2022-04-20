
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] % 2 == 1:
        a[i] -= 1
        ans += 1

if sum(a) // k < 2:
    print(ans) # 가지고 있는 수들을 하나씩 빼는 연산만 해도 음수가 되므로 이렇게 가장 적은 연산을 하는 것이 최선이다.
else:
    print(ans + sum(a) // k - 1) # 이렇게 하는 이유는 가장 적은 연산을 하기 위해서이다.
