
import sys

N = int(input())

# get the number of bills
num_of_bills = N // 10000

# get the amount of change
change = 10000 * num_of_bills - N

print(change)
