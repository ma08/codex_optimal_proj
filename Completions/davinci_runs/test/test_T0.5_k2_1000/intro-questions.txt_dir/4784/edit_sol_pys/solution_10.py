

# Number of megabytes per month.
X = int(input())
# Number of months.
N = int(input())
# Megabytes per month.
megabytes = [int(input()) for i in range(N)]

# Total megabytes used.
total_megabytes = sum(megabytes)
# Megabytes left over.
megabytes_left = X - total_megabytes

# Total megabytes after N months.
total_megabytes_after_N_months = total_megabytes + megabytes_left

print(total_megabytes_after_N_months)
