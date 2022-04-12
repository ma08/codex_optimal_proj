

# The solution is to check if the year is even and if the year is divisible by 4.
year = int(input())
if year % 2 == 0 and year % 4 == 0:
    print("yes")
else:
    print("no")
