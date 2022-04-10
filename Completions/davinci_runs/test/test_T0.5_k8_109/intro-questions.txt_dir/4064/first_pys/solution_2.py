

def get_max_good_times(n, h, l, r, a):
    good_times = 0
    for i in range(n):
        if l <= a[i] % h <= r:
            good_times += 1
            a[i] += 1
        else:
            a[i] += 2
    return good_times

if __name__ == "__main__":
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_max_good_times(n, h, l, r, a))