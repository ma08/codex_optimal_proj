

def check_constraints(p):
    for i in range(len(p)-1):
        if p[i+1] - p[i] not in [2,3,4]: # check if there are any gaps
            return False
    return True

def get_permutation(n):
    if n == 2:
        return [-1]
    elif n == 3:
        return [3,1,2]
    elif n == 4:
        return [3,1,4,2]
    elif n == 5:
        return [5,3,1,4,2]
    else:
        p = [5,3,1,4,2] # base case, n = 5
        for i in range(5,n+1): # recursion, n > 5
            p.append(p[len(p)-1] + 2) # add the next number to the end of the list
        return p

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        p = get_permutation(n)
        if p[0] == -1: # if there are no possible permutations
            print(-1)
        else:
            print(*p)

main()
