
def main():
    n, m = map(int, input().split())
    k = list(map(int, input().split()))
    d_t = [list(map(int, input().split())) for _ in range(m)]
    k_sum = sum(k)
    d_t_dict = {i + 1: 0 for i in range(n)}
    for d, t in d_t:
        d_t_dict[t] += 1
    d_t_dict = sorted(d_t_dict.items(), key=lambda x: x[1])
    k = sorted(k, reverse=True)
    d = 0
    while k_sum != 0:
        d += 1
        if d_t_dict[0][0] == d:
            k_sum -= k[0]
            k.pop(0)
            d_t_dict.pop(0)
        else:
            k_sum -= sum(k)
            k = []
    print(d)


if __name__ == '__main__':
    main()
