

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    # print(n, a)
    n_teams = n // 2
    n_problems = 0
    for i in range(n_teams):
        a_i = a[i]
        if a_i > n_teams:
            n_problems += a_i - n_teams
    print(n_problems)

if __name__ == '__main__':
    main()