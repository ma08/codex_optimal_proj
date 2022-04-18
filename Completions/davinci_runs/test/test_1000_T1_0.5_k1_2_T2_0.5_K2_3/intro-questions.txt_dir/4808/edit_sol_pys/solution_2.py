

#gets input
num_years, current_year_days = map(int, input().split())

#gets list of days
days_list = list(map(int, input().split()))

#creates counter, sets it to 0
counter = 0

#uses a for loop
for i in days_list:
    #if the current year days is smaller than the current days
    if current_year_days < i:
        #prints the current counter
        print("It hadn't snowed this early in {} years!".format(counter + 1))
        #exits the loop
        exit()
    #adds to the counter, breaks the loop if the counter is equal to the number of years
    counter += 1 if counter < num_years - 1 else exit()
#prints the counter
print("It had never snowed this early!")
