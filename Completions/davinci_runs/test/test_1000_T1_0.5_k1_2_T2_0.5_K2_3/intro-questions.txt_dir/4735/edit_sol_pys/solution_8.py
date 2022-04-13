

# The solution is to check whether the year is even and if the year is divisible by 26.
year = int(input())
if year % 2 == 0 and year % 26 == 0:
    print("yes")
else:
    print("no")
