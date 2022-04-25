
N, K = map(int, input().split())
a = [int(i) for i in input().split()]
print(sum([1 if i >= K else 0 for i in a]))
