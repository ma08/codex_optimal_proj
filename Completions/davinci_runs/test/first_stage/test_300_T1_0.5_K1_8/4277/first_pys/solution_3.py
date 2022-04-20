

import sys

N, A, B = map(int, input().split())

# If N people take the train, it will cost N * A yen.
# If N - 1 people take the train, the cost will be (N - 1) * A yen.
# The remaining person will take the taxi and pay B yen.
# The total cost will be (N - 1) * A + B yen.
# We can calculate the minimum total travel expense by comparing N * A and (N - 1) * A + B.

print(min(N * A, (N - 1) * A + B))