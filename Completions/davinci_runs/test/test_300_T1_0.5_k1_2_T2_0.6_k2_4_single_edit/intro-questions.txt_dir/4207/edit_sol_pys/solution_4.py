import bisect

def solve(a, b):
    c = [a1+b1 for a1, b1 in zip(a, b)]
    c.sort()
    zero_idx = bisect.bisect_right(c, 0)
    return zero_idx + (len(c) - zero_idx)


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(solve(a, b))
