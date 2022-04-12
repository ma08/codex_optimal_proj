

# Process:
# 1. Read the input
# 2. Compute the days of the week
# 3. Output the result

# 1.
d_m = input().split()  # split the input into a list of two strings
d = int(d_m[0])  # convert the first string to an integer
m = int(d_m[1])  # convert the second string to an integer

# 2.
days = {  # a dictionary of days of the week
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

days_in_month = {  # a dictionary of days in each month
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

# 3.
day_of_week = 4  # 1 Jan 2009 is a Thursday
for m_i in range(1, m):  # for each month before the input month
    day_of_week += days_in_month[m_i]  # add the number of days in that month to the day of the week
day_of_week += d  # add the number of days in the input month to the day of the week
day_of_week %= 7  # modulo 7 to get the day of the week

print(days[day_of_week])  # output the day of the week
