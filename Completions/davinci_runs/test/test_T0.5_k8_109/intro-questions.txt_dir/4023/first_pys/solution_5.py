
n = int(input())
a = list(map(int, input().split()))

if len(set(a)) == 1:
    print("YES")
    exit(0)

if len(set(a)) == 2:
    a_max = max(a)
    a_min = min(a)
    max_count = a.count(a_max)
    min_count = a.count(a_min)
    if a_max - a_min == 1:
        if max_count == 1 and min_count == n-1:
            print("YES")
            exit(0)
        elif max_count == 2 and min_count == n-2:
            print("YES")
            exit(0)
        elif max_count == n-1 and min_count == 1:
            print("YES")
            exit(0)
        elif max_count == n-2 and min_count == 2:
            print("YES")
            exit(0)
    else:
        print("NO")
        exit(0)

print("NO")