

def check_constraints(p):
    for i in range(len(p)-1):
        if p[i + 1] - p[i] not in [2, 3, 4]:
            return False
    return True


def get_permutation(n):
    if n == 2:
        return []
    elif n == 3:
        return [3, 1, 2]
    elif n == 4:
        return [3, 1, 4, 2]
    elif n == 5:
        return [5, 3, 1, 4, 2]
    else:
        for i in range(5, n + 1):
            p.append(p[len(p) - 1] + 2)
        return p


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        p = get_permutation(n)
        if len(p) == 0:
            print(-1)
        else:
            print(*p)


main()
