

N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()

print(H[-K])
