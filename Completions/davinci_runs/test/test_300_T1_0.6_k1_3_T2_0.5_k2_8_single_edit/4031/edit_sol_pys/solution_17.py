from collections import Counter


def solve(s):
    c = Counter(s)
    odd = 0
    for k, v in c.items():
        if v % 2 == 1:
            odd += 1
    if odd > 1:
        return 'NO SOLUTION'
    ret = ''
    for k, v in c.items():
        if v % 2 == 1:
            ret = k
            c[k] -= 1
        for _ in range(v // 2):
            ret = k + ret + k
    return ret

def main():
    s = input()
    print(solve(s))

if __name__ == '__main__':
    main()
