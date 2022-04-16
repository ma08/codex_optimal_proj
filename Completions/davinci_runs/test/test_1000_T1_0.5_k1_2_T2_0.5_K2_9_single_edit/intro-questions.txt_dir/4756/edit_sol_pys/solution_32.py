

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

        # Find the line that minimizes the total unusefulness of the
        # citizens to the left and right of the line
        left_line = citizens[mid-1][1] - citizens[mid-1][0]
        right_line = citizens[mid][1] - citizens[mid][0]

        if left_line == right_line:
            return left_line
        elif left < right:
            return left
        else:
            return right

print(min_a(citizens))
