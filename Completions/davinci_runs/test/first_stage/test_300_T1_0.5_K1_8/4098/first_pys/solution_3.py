

def main():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))

	# Sort the list
	a.sort()

	# Initialize the number of students in each team
	students_in_teams = [0] * k

	# Initialize the number of teams
	num_teams = 0

	# Iterate through the list
	for i in range(n):
		# Check if the number of teams is less than k
		if num_teams < k:
			# Add the student to the team
			students_in_teams[num_teams] += 1
			# Increment the number of teams
			num_teams += 1
		else:
			# Iterate through the students in each team
			for j in range(k):
				# Check if the difference between the student and the last student in the team is less than or equal to 5
				if a[i] - a[i - students_in_teams[j]] <= 5:
					# Add the student to the team
					students_in_teams[j] += 1
					# Break out of the loop
					break

	# Print the maximum number of students in the teams
	print(max(students_in_teams))

if __name__ == "__main__":
	main()