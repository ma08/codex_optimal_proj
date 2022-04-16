

import math

m, n, time_complexity_type = map(int, input().split())

# Calculate the time complexity
if time_complexity_type == 1:
    time_complexity = n
elif time_complexity_type == 2:
    time_complexity = 2**n
elif time_complexity_type == 3:
    time_complexity = n**4
elif time_complexity_type == 4:
    time_complexity = n**3
elif time_complexity_type == 5:
    time_complexity = n**2
elif time_complexity_type == 6:
    time_complexity = n*(math.log(n, 2))
elif time_complexity_type == 7:
    time_complexity = n

# Check if the time complexity is less than or equal to m
if time_complexity <= m:
    print("AC")
else:
    print("TLE")
