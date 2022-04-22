import itertools

import sys

def main():
    try:
        N = int(sys.stdin.readline())
        names = [sys.stdin.readline().strip() for _ in range(N)]
        dic = {}
        for name in names:
            if name[0] in dic:
                dic[name[0]] += 1
            else:
                dic[name[0]] = 1
        keys = list(dic.keys())
        ans = sum([dic[i] * dic[j] * dic[k] for i, j, k in itertools.combinations(keys, 3)])
        print(ans)
    except:
        print(0)


if __name__ == '__main__':
    main()
