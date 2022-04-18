import sys

# Get the number of subjects, the maximum score, and the goal score.
N, K, M = map(int, input().split())

# Get the scores on the previous exams
scores = list(map(int, input().split()))

# The lowest possible score is the goal score, since we only need to find a score that meets or exceeds the goal.
# The highest possible score is the maximum score.
lowest_score = M
highest_score = K

# As long as the lowest score is less than the highest score, we can keep checking.
while lowest_score < highest_score:
    # Calculate the average of the lowest and highest scores.
    middle_score = (lowest_score + highest_score) // 2

    # Calculate the total score, if the final score was middle_score.
    total = sum(scores) + middle_score

    # If the total score is at least N times the goal score, we know that we can achieve the goal by scoring middle_score on the final subject. 
    if total >= N * M:
        # Set the highest possible score to the middle score.
        highest_score = middle_score
    # If the total score is less than N times the goal score, we know that we cannot achieve the goal by scoring middle_score on the final subject.
    else:
        # Set the lowest possible score to 1 greater than the middle score.
        lowest_score = middle_score + 1

# If the lowest score is greater than or equal to the maximum score, we cannot achieve the goal.
if lowest_score >= K:
    print(-1)
# Otherwise, the lowest score is the minimum score we need to get on the final subject.
else:
    print(lowest_score)
