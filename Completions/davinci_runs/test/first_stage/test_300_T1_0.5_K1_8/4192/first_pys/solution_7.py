

# get input from user
D, T, S = map(int, input().split())

# calculate time needed to arrive at the place
time_needed = D / S

# check if he can arrive in time
if time_needed <= T:
    print("Yes")
else:
    print("No")