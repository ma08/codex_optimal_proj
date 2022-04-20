

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 全ての課題をこなすために必要な日数
days_needed = sum(A)

if days_needed > N:
    print(-1)
else:
    print(N - days_needed)