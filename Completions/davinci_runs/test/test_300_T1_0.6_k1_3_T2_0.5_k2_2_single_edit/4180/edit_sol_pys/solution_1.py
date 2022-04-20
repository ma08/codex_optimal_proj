import sys
N = int(input())
num_of_bills = N // 1000
change = 1000 * num_of_bills - N
print(change)

