

def main():
    n = int(input())
    day = 1
    num_printers = 1  # number of printers
    num_statues = 0  # number of statues
    while num_statues < n:  # while number of statues is less than the number of statues we want
        num_statues += num_printers  # each day, we add the number of printers to the number of statues we have
        num_printers += 1  # each day we get one printer more
        day += 1
    print(day)


if __name__ == "__main__":
    main()
