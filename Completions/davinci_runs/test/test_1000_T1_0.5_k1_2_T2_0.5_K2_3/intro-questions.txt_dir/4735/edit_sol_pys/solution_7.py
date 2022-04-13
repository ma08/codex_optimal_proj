

# The solution is to check if the year is even and if the year is divisible by 25.
year = int(input())
if year % 2 == 0 and year % 25 == 0:
    print("yes")
else:
    print("no")
