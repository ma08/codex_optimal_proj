

def solve(n, wall):
    # Complete this function
    if (len(set(wall)) == 1): # if all the values in the list are the same
        return "YES"
    elif (len(set(wall)) == 2): # if there are two values in the list
        a = wall.count(max(wall))
        b = wall.count(min(wall))
        if (a == 1 and b == 1): # if the two values occur only once
            return "NO"
        else: # if the two values occur more than once
            return "YES"
    else: # if there are more than two values in the list
        return "NO"

n = int(input().strip())
wall = list(map(int, input().strip().split(' ')))
print(solve(n, wall))
