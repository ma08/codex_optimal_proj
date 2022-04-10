
def leap_year(n):
    return 1 if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0 else 0

if __name__ == "__main__":
    print(leap_year(int(input())))
