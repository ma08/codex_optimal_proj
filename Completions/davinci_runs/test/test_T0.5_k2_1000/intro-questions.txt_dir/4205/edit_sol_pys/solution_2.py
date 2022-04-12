N = int(input())
sequence = list(map(int, input().split()))  # input sequence

if sequence == sorted(sequence):
    print("YES")
else:
    print("NO")

# input
# 5
# 1 2 3 4 5

# output
# YES
