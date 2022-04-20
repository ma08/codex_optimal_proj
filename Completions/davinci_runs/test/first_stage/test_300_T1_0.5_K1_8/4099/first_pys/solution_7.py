

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

def main():
    sum_a = sum(a)
    min_points_needed = m * n - sum_a
    if min_points_needed > k:
        print(-1)
    else:
        print(max(0, min_points_needed))

if __name__ == '__main__':
    main()