

def is_leap_year(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

for i in range(n // 4 + 1):
    if (n - 4 * i) % 7 == 0:
        print("Yes")
        sys.exit()

print("No")
