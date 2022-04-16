

#gets input, splits it into a list
input_list = input().split()

#sets the number of years to the first value in the list
num_years = int(input_list[0])

#sets the current year days to the second value in the list
current_year_days = int(input_list[1])

#gets input, splits it into a list
days_list = input().split()

#creates a list for the days
days_list_int = []

#for loop for the days list
for i in days_list:
    #appends the int value of the current index to an int list
    days_list_int.append(int(i))

#creates counter, sets it to 0
counter = 0

#creates while loop
while counter < num_years:
    #if the counter is larger than the current year days
    if days_list_int[counter] > current_year_days:
        #prints the counter
        print("It hadn't snowed this early in {} years!".format(counter))
        #breaks the loop
        break
    #if the counter is equal to the number of years
    elif counter == num_years - 1:
        #prints the counter
        print("It had never snowed this early!")
        #breaks the loop
        break
    #adds to the counter
    counter += 1
