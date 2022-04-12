
import sys

# Open input file and get number of cases
with open(sys.argv[1]) as f:
    num_cases = int(f.readline())

    # Loop through each case
    for i in range(num_cases):
        # Get the current case
        case = f.readline().split()
        # Get the direction of the time change (forward or backward)
        direction = case[0]
        # Get the amount of time to change (in minutes)
        time_change = int(case[1])
        # Get the current hour (24 hour time)
        current_hour = int(case[2])
        # Get the current minute (24 hour time)
        current_min = int(case[3])

        # If we are going forward in time (F)
        if direction == 'F':
            # Check if we will go over an hour
            if current_min + time_change >= 60:
                # Get the number of hours we will go over
                hours_over = (current_min + time_change) // 60
                # Get the new hour
                new_hour = (current_hour + hours_over) % 24
                # Get the new minute
                new_min = (current_min + time_change) % 60
                # Print the new time
                print(new_hour, new_min)
            # If we are not going over an hour
            else:
                # Get the new hour
                new_hour = current_hour
                # Get the new minute
                new_min = current_min + time_change
                # Print the new time
                print(new_hour, new_min)
        # If we are going backward in time
        else:
            # Check if we will go under an hour
            if current_min - time_change < 0:
                # Get the number of hours we will go under
                hours_over = (current_min - time_change) // 60
                # Get the new hour
                new_hour = (current_hour + hours_over) % 24
                # Get the new minute
                new_min = (current_min - time_change) % 60
                # Print the new time
                print(new_hour, new_min)
            # If we are not going under an hour 
            else:
                # Get the new hour
                new_hour = current_hour
                # Get the new minute
                new_min = current_min - time_change
                # Print the new time
                print(new_hour, new_min)
