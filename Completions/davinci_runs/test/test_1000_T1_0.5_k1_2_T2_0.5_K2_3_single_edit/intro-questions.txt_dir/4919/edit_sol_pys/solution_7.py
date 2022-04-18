

from collections import defaultdict, Counter


def get_ans(trips, c, k):
    if c not in trips or k > len(trips[c]):
        return -1
    return trips[c][k - 1]


n = int(input())
trips = defaultdict(list)

for _ in range(n):
    c, y = input().split()
    trips[c].append(int(y))

q = int(input())

for _ in range(q):
    c, k = input().split()
    print(get_ans(trips, c, int(k)))
