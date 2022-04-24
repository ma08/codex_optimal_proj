import sys

# Get the number of subjects, the maximum score, and the minimum score
N, K, M = map(int, sys.stdin.readline().strip().split())

# Get the scores on the previous exams
scores = list(map(int, sys.stdin.readline().strip().split()))

# The lowest possible score is the minimum score, since we only need to find a score that meets or exceeds the minimum.
# The highest possible score is the maximum score.
lowest_score = M - 1
highest_score = K

# As long as the lowest score is less than the highest score, we can keep checking.
while lowest_score < highest_score:
    # Calculate the average of the lowest and highest scores
    middle_score = (lowest_score + highest_score) // 2

    # Calculate the total score, if the final score was middle_score + 1.
    total = sum(scores) + middle_score

    # If the total score is at least N times the minimum score, we know that we can achieve the minimum by scoring middle_score + 1 on the final subject.
    if total >= N * M:
        # Set the highest possible score to the middle score.
        highest_score = middle_score
    # If the total score is less than N times the minimum score, we know that we cannot achieve the minimum by scoring middle_score + 1 on the final subject.
    else:
        # Set the lowest possible score to the middle score + 1.
        lowest_score = middle_score + 1

# If the lowest score is greater than or equal to the maximum score, we cannot achieve the minimum.
if lowest_score >= K:
    print(-1)
# Otherwise, the lowest score + 1 is the minimum score we need to get on the final subject.
else:
    print(lowest_score + 1)
