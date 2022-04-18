

#Number of megabytes per month
x = int(input())
#Number of months
n = int(input())
#Megabytes per month
megabytes = [int(input()) for i in range(n)]

#Total megabytes used
total_megabytes = sum(megabytes)
#Megabytes left over
megabytes_left = x - total_megabytes

#Total megabytes after N months
total_megabytes_after_N_months = total_megabytes + megabytes_left

print(total_megabytes_after_N_months)
