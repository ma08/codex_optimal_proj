def solution(y):
    if y % 26 == 2 or y % 26 == 18:
        return "yes"
    else:
        return "no"

# Read input
y = int(input().strip())

# Determine if optimal launch window occurs in year y
print(solution(y))
