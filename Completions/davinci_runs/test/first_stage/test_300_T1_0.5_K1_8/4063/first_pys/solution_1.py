

from collections import Counter

N = int(input())
d = list(map(int, input().split()))

d_counter = Counter(d)

# The number of problems for ARCs and the number of problems for ABCs will be the same if and only if the total number of problems is even and the number of problems with difficulty K is even.

# The total number of problems is even if and only if N is even.
if N % 2 == 1:
    print(0)
else:
    # The number of problems with difficulty K is even if and only if the number of problems with difficulty K is even.
    count_even = 0
    for k, v in d_counter.items():
        if v % 2 == 0:
            count_even += 1
    print(count_even)