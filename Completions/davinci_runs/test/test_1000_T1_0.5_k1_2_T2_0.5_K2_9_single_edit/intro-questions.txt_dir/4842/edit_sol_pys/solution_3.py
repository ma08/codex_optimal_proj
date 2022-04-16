import sys

def main():
    v = list(map(int, sys.stdin.readline().split()))  # v: [n, v1, v2, ..., vn]
    d = 0  # d: degree
    while True:
        d += 1
        v_diff = []
        for i in range(len(v) - 1):
            v_diff.append(v[i + 1] - v[i])
        v = v_diff
        if len(set(v)) == 1:
            break
    print(d, v[0] * d + v[0])

if __name__ == '__main__':
    main()
