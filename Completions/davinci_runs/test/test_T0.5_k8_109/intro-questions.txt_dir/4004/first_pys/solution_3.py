

def solve(a):
    if len(a) == 1:
        return 0

    min_val, max_val = min(a), max(a)
    if min_val == max_val:
        return 0

    if min_val + 1 == max_val:
        return 1

    return -1

if __name__ == '__main__':
    n = int(raw_input())
    a = [int(x) for x in raw_input().split()]
    print solve(a)