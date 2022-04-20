

N = int(input())
A = list(map(int, input().split()))

# A is the number of students in the classroom when each student entered the classroom, including themselves
# So, we can use A as a key to sort the students
# The student with the smallest number of students when they entered the classroom must have entered first
# (because they have the smallest number of students when they entered the classroom)
# The student with the second smallest number of students when they entered the classroom must have entered second
# (because they have the second smallest number of students when they entered the classroom)
# And so on...

# We can use the value of A as the key to sort the students
# We can use the index of A as the student number
# So, we can zip the two lists together and sort by A

# We can then unzip the lists and print the student numbers

# Create a list of tuples where each tuple is (A, index)
# Sort by A
# Unzip the list of tuples into two lists
# Print the student numbers
print(*[b for a, b in sorted(zip(A, range(1, N + 1)))])

"""
-----Test Cases-----

(Test Case 1)
Input:
3
2 3 1

Output:
3 1 2

(Test Case 2)
Input:
5
5 3 2 4 1

Output:
1 4 2 5 3

(Test Case 3)
Input:
6
3 5 6 1 2 4

Output:
4 2 6 1 5 3

(Test Case 4)
Input:
10
1 2 3 4 5 6 7 8 9 10

Output:
1 2 3 4 5 6 7 8 9 10
"""