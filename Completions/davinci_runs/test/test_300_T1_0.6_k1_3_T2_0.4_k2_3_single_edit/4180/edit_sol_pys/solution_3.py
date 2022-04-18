
import sys

N = int(input())

# get the number of 5-yen coins
num_of_coins = N // 5

# get the amount of change
change = 5 * num_of_coins - N

print(change)
