

# Process
# 1. Read the input
# 2. Compute the days of the week
# 3. Output the result

# 1.
d_m = input().split()
d = int(d_m[0])
m = int(d_m[1])

# 2.
days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# 1 Jan 2009 is a Thursday
# 2 Jan 2009 is a Friday
# 3 Jan 2009 is a Saturday
# 4 Jan 2009 is a Sunday
# 5 Jan 2009 is a Monday
# 6 Jan 2009 is a Tuesday
# 7 Jan 2009 is a Wednesday

# 3.
day_of_week = 4
for m_i in range(1, m):
    day_of_week += days_in_month[m_i]
day_of_week += d
day_of_week %= 7

print(days[day_of_week])
