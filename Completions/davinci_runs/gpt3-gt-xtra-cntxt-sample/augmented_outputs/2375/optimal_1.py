from collections import Counter

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a_counter = Counter(a)
    a_max = max(a_counter, key = a_counter.get)
    max_len = a_counter[a_max]
    if a_counter[a_max] >= 2:
        max_len = max_len + 1
    print(max_len)