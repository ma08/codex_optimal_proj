

N = int(input())
citizens = []
for i in range(N):
    x, y = [int(s) for s in input().split()]
    citizens.append([x, y])

# Find the smallest value of a that minimizes the total unusefulness
# for a given set of citizens
def min_a(citizens):
    if len(citizens) == 0:
        return 0
    elif len(citizens) == 1:
        return citizens[0][1] - citizens[0][0]
    else:
        # Sort the citizens by x-coordinate
        citizens.sort()

        # Find the line that minimizes the total unusefulness of the
        # citizens to the left and right
        mid = len(citizens) // 2
        left = min_a(citizens[:mid])
        right = min_a(citizens[mid:])

        # Find the line that minimizes the total uselessness of the
        # citizens to the left and right of the line
        left_line = citizens[mid-1][1] - citizens[mid-1][0]
        right_line = citizens[mid][1] - citizens[mid][0]

        # Note: The following line does not work in the case where
        # the left and right lines are the same
        #mid_line = (left_line + right_line) / 2
        mid_line = left_line + (right_line - left_line) / 2

        # Find the line that minimizes the total uselessness of the
        # citizens to the left and right of the line
        mid_left = mid_line
        mid_right = mid_line + 1
        mid_left_total = 0
        mid_right_total = 0
        for citizen in citizens[:mid]:
            mid_left_total += citizen[1] - (citizen[0] + mid_left)
        for citizen in citizens[mid:]:
            mid_right_total += citizen[1] - (citizen[0] + mid_right)

        # Find the line that minimizes the total uselessness of the
        # citizens to the left and right of the line
        if left_line == right_line:
            return min(left, right)
        elif mid_left_total < mid_right_total:
            return min(left, mid_left)
        else:
            return min(right, mid_right)

print(min_a(citizens))
