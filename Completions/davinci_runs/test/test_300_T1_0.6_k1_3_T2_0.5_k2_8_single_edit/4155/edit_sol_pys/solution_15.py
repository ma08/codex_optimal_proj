
N = int(input())
h = list(map(int, input().split()))
print(sum(abs(h[i] - (i + 1)) for i in range(N)))
