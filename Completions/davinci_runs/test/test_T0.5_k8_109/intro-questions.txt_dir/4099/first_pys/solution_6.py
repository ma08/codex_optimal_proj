

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, m, a))

def solve(n, k, m, a):
    total = sum(a)
    min_score = (n * m) - total
    if min_score > k:
        return -1
    else:
        return min(min_score, k)

if __name__ == '__main__':
    main()