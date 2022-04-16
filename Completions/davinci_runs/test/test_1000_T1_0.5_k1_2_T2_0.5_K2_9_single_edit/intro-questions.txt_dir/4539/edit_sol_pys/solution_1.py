

def get_max(d):
    max_key = max(d, key=lambda k: d[k])
    return max_key, d[max_key]

if __name__ == '__main__':
    n = int(input())
    d = {}
    for _ in range(n):
        a, b = [int(x) for x in input().split()]
        if a in d:
            d[a] += b
        else:
            d[a] = b
    print(' '.join([str(x) for x in get_max(d)]))
