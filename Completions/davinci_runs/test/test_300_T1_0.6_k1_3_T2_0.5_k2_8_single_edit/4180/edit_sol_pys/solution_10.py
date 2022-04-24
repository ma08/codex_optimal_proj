N = int(input())

# get the number of 1000-yen bills
num_of_bills = N // 1000

# get the amount of change
change = 1000 * num_of_bills - N

print(change)
