
import sys

N = int(input())

# get the number of 500-yen coins
num_of_coins = N // 500

# get the amount of change
change = 500 * num_of_coins - N

print(change)
