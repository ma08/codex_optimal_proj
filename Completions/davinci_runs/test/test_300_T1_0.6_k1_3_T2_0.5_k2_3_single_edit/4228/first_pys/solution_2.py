

#!/usr/bin/env python3

n, l = list(map(int, input().split()))

# The optimal choice is to eat the apple with the smallest absolute difference from the average flavor of all apples.
# The average flavor of all apples is (l + l+n-1) / 2.
print(sum([l+i for i in range(n-1)]) - (l + l+n-1) // 2 * n)