

N = int(input())
A = list(map(int, input().split()))

# A[i] = j means that j students entered the classroom before student i entered the classroom.
# Therefore, the student who entered the classroom first is the student who has A[i] = 0.
# The student who entered the classroom second is the student who has A[i] = 1.
# The student who entered the classroom third is the student who has A[i] = 2.
# ...
# The student who entered the classroom N-th is the student who has A[i] = N-1.
# Therefore, we can find the order of the students by sorting A in ascending order.

# Sort A in ascending order.
A.sort()

# Print the student numbers of the students in the order the students entered the classroom.
for i in range(N):
    print(A[i])