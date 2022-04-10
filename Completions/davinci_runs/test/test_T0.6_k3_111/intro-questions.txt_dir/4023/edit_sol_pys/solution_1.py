

def solve_problem(a):
    max_a = max(a)
    min_a = min(a)
    diff = max_a - min_a
    if diff == 0:
        return 'YES'
    elif diff % 2 == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    n = int(input())
    a = input().split()
    for i in range(n):
        a[i] = int(a[i])

    print(solve_problem(a))
