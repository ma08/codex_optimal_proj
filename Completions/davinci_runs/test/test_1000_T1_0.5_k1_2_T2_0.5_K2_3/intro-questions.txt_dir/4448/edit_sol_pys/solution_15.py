
def main():
    n, m = map(int, input().split())
    k = list(map(int, input().split()))
    dt = [list(map(int, input().split())) for _ in range(m)]
    k_sum = sum(k)
    dt_dict = {i+1: 0 for i in range(n)}
    for d, t in dt:
        dt_dict[t] += 1
    dt_dict = sorted(dt_dict.items(), key=lambda x: x[1], reverse=True)
    k = sorted(k, reverse=True)
    d = 0
    while k_sum != 0:
        d += 1
        if dt_dict[0][1] == 0:
            dt_dict.pop(0)
        elif dt_dict[0][0] == d:
            k_sum -= k[0]
            k.pop(0)
            dt_dict.pop(0)
        else:
            k_sum -= sum(k)
            k = []
    print(d)


if __name__ == '__main__':
    main()
