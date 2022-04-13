
from bisect import bisect_left

n, m = map(int, input().split())  # n - number of dorms, m - number of queries
a = list(map(int, input().split()))  # a[i] - number of students in the i-th dorm
b = list(map(int, input().split()))  # queries

dorm_sums = [0]  # cumulative sum of students in the dorms
for i in range(n):
    dorm_sums.append(dorm_sums[i] + a[i])

# find the first dorm where cumulative sum of students >= query
for query in b:
    i = bisect_left(dorm_sums, query)
    print(i, query - dorm_sums[i-1])  # i - dorm number, query - dorm_sums[i-1] - number of students in the dorms with number < i
