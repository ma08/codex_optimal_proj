
def get_input():
    return [int(x) for x in input().split()], int(input())



def solve(n, m, cnt=0):
    if n == m:
        return cnt
    if n > m:
        return -1
    if m % n != 0:
        return -1
    return solve(n * 2, m, cnt + 1) if m % (n * 2) == 0 else solve(n * 3, m, cnt + 1)


if __name__ == '__main__':
    n, m = get_input()[0]
    print(solve(n, m))
