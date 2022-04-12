

def check_constraints(p):
    for i in range(len(p)-1):
        if p[i+1] - p[i] not in [2,3,4]:
            return False
    return True

def get_permutation(n):
    if n == 2:
        return [2,1]
    elif n == 3:
        return [3,2,1]
    elif n == 4:
        return [3,2,4,1]
    elif n == 5:
        return [5,3,2,4,1]
    else:
        p = [5,3,2,4,1] # base case
        for i in range(5,n+1): # recursion
            p.append(p[len(p)-1] + 1)
        return p

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        p = get_permutation(n)
        print(*p)

main()
