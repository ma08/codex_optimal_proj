

def get_permutation(n):
    if n == 2:
        return [1,2]
    elif n == 3:
        return [1,3,2]
    elif n == 4:
        return [1,3,4,2]
    elif n == 5:
        return [1,5,3,4,2]
    else:
        p = [1,5,3,4,2]
        for i in range(5,n+1):
            p.append(p[len(p)-1] + 2)
        return p

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        p = get_permutation(n)
        print(*p)

main()
