


def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    c = Counter(p)
    c_keys = sorted(c.keys())
    c_values = sorted(c.values())
    c_values = list(map(lambda x: x//2, c_values))

    c_idx = 0
    c_sum = 0
    while c_sum < m:
        c_sum += c_values[c_idx]
        c_idx += 1

    c_idx -= 1
    c_sum -= c_values[c_idx]

    ans = 0
    for i in range(c_idx, n):
        if c_keys[i] > m:
            break
        if c_keys[i] == m:
            ans += c_values[i]**2

    for i in range(c_idx):
        if c_keys[i] >= m:
            break
        if c_keys[i] == m:
            ans += c_values[i]**2

    for i in range(c_idx):
        for j in range(c_idx, n):
            if c_keys[i] + c_keys[j] < 2*m:
                ans += c_values[i]*c_values[j]
            else:
                break

    print(ans)


if __name__ == '__main__':
    main()