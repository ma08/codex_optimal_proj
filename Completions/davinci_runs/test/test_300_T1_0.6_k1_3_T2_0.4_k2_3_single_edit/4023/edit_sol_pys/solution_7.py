

def solve(n, wall):
    if (len(set(wall)) == 1):
        return "YES"
    elif (len(set(wall)) == 2):
        a = wall.count(max(wall)) # count the number of max values
        b = wall.count(min(wall)) # count the number of min values
        if (a == 1 and b == 1): # if there is only one max and one min value
            return "NO"
        else: # if there is more than one max or more than one min value
            return "YES"
    else: # if there are more than 2 different values
        return "NO"

n = int(input().strip())
wall = list(map(int, input().strip().split(' ')))
print(solve(n, wall))
