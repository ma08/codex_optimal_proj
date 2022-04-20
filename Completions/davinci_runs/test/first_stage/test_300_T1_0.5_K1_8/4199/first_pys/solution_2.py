

N, K = map(int, input().split())
h = [int(i) for i in input().split()]

print(len([i for i in h if i >= K]))