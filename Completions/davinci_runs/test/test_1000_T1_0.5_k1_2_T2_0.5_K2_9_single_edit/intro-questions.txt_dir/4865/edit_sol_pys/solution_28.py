

# Get the number of test cases
num_cases = int(input())

# Iterate through each test case
for case in range(num_cases):
	# Get the input for each test case
	direction, change, hour, minute = input().split() # Get the input for each test case
	change = int(change) # Convert the change to an integer
	hour = int(hour) # Convert the hour to an integer
	minute = int(minute) # Convert the minute to an integer

	# Add or subtract the number of minutes to change by
	if direction == 'F':
		minute += change # Add the change to the minute
	else:
		minute -= change # Subtract the change from the minute

	# If the minutes are negative, we need to add 60 to the minute and subtract 1 from the hour
	# If the minutes are greater than 60, we need to subtract 60 from the minute and add 1 to the hour
	if minute < 0:
		minute += 60 # Add 60 to the minute
		hour -= 1 # Subtract 1 from the hour
	elif minute > 60:
		minute -= 60 # Subtract 60 from the minute
		hour += 1 # Add 1 to the hour

	# If the hour is negative, we need to add 24 to the hour
	# If the hour is greater than 24, we need to subtract 24 from the hour
	if hour < 0:
		hour += 24 # Add 24 to the hour
	elif hour > 24:
		hour -= 24 # Subtract 24 from the hour

	# Print the resulting hour and minute
	print(hour, minute)
