
# Define the function
def dst_calculator(direction, minutes, hour, minute):

    # Add the minutes to the current time
    if direction == "F":
        minute += minutes
    elif direction == "B":
        minute -= minutes

    # If the minutes are greater than 60, then add an hour and subtract 60 minutes
    if minute > 59:
        hour += 1
        minute -= 60
    # If the minutes are less than 0, then subtract an hour and add 60 minutes
    elif minute < 1:
        hour -= 1
        minute += 60

    # If the hour is greater than 24, then subtract 24 hours
    if hour > 23:
        hour -= 24
    # If the hour is less than 0, then add 24 hours
    elif hour < 1:
        hour += 24

    # Print the hour and minute
    if hour < 10:
        if minute < 10:
            print("0" + str(hour) + ":" + "0" + str(minute))
        else:
            print("0" + str(hour) + ":" + str(minute))
    else:
        if minute < 10:
            print(str(hour) + ":" + "0" + str(minute))
        else:
            print(str(hour) + ":" + str(minute))

# Get the number of tests
tests = int(input())

# Loop through the tests
for i in range(tests):
    # Get the inputs
    direction, minutes, hour, minute = input().split(":")
    minutes = int(minutes)
    hour = int(hour)
    minute = int(minute[:2])
    # Run the function
    dst_calculator(direction, minutes, hour, minute)
