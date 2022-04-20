
import sys

# Get the number of subjects and the goal score
N, M = map(int, sys.stdin.readline().split())

# Get the scores on the previous exams
scores = list(map(int, sys.stdin.readline().split()))

# The highest possible score is the goal score, since we only need to find a score that meets or exceeds the goal.
# The lowest possible score is the sum of all the scores.
highest_score = M
lowest_score = sum(scores)

# As long as the lowest score is less than the highest score, we can keep checking.
while lowest_score < highest_score:
    # Calculate the average of the highest and lowest scores
    middle_score = (highest_score + lowest_score) // 2

    # Calculate the total score, if the final score was middle_score
    total = middle_score * N

    # If the total score is at least N times the goal score, we know that we can achieve the goal by scoring middle_score on the final subject.
    if total >= N * M:
        # Set the lowest possible score to the middle score
        lowest_score = middle_score
    # If the total score is less than N times the goal score, we know that we cannot achieve the goal by scoring middle_score on the final subject.
    else:
        # Set the highest possible score to 1 less than the middle score
        highest_score = middle_score - 1

# If the lowest score is less than or equal to the sum of all the scores, we cannot achieve the goal.
if lowest_score <= sum(scores):
    print(-1)
# Otherwise, the lowest score is the minimum score we need to get on the final subject
else:
    print(lowest_score - sum(scores))
