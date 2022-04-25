
N, K = map(int, input().split())
a = [int(i) for i in input().split()]
print(sum(1 for i in a if i >= K))
