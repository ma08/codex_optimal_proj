

N, A, B, C, D, E = map(int, input().split())

# print(N, A, B, C, D, E)

def calc_time(n, a, b, c, d, e):
    time = 0
    while n > 0:
        if n > A:
            n -= A
            time += 1
        elif n > B:
            n -= B
            time += 1
        elif n > C:
            n -= C
            time += 1
        elif n > D:
            n -= D
            time += 1
        elif n > E:
            n -= E
            time += 1
        else:
            time += 1
            break
    return time

time = calc_time(N, A, B, C, D, E)
print(time)