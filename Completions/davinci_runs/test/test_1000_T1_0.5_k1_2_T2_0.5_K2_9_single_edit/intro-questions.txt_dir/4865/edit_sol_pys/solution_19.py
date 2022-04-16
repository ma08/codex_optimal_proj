

# Get the number of test cases
num_cases = int(input())

# Iterate through each test case
for case in range(num_cases):
	# Get the input for each test case
	direction, change, hour, minute = input().split()
	change = int(change)
	hour = int(hour)
	minute = int(minute)

	# Add or subtract the number of minutes to change by
	if direction == 'F':
		minute += change
	else:
		minute -= change

	# If the minutes are negative, we need to add 60 to the minute and subtract 1 from the hour
	# If the minutes are greater than 60, we need to subtract 60 from the minute and add 1 to the hour
	if minute < 0:
		minute += 60
		hour -= 1
	elif minute > 60:
		minute -= 60
		hour += 1

	# If the hour is negative, we need to add 24 to the hour
	# If the hour is greater than 24, we need to subtract 24 from the hour
	if hour < 0:
		hour += 24
	elif hour > 24:
		hour -= 24

	# Print the resulting hour and minute
	print(str(hour) + " " + str(minute))
