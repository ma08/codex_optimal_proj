
N, K = map(int, input().split()) # N桁の整数K
D = set(map(int, input().split())) # 整数の不足している数字

# print(N, K, D)

for i in range(N, 10000):
    if all(d not in str(i) for d in D): # all(iterable) -> True if all elements of the iterable are true (or if the iterable is empty)
        print(i)
        break
