

# gets input
num_years, current_year_days = map(int, input().split())

# gets list of days
days_list = list(map(int, input().split()))

# creates counter, sets it to 0
counter = 0

# creates while loop
while counter < num_years:
    # if the counter is larger than the current year days
    if days_list[counter] > current_year_days:
        # prints the counter
        print("It hadn't snowed this early in {} years!".format(counter))
        # breaks the loop
        break
    # if the counter is equal to the number of years
    elif counter == num_years - 1:
        # prints the counter
        print("It had never snowed this early!")
        # breaks the loop
        break
    # adds to the counter
    counter += 1
