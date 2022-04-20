
import sys

def main():
    N = int(sys.stdin.readline())
    names = [sys.stdin.readline().strip() for _ in range(N)]
    dic = {}
    for name in names:
        if name[0] in dic:
            dic[name[0]] += 1
        else:
            dic[name[0]] = 1
    keys = dic.keys()
    ans = 0
    for i, key1 in enumerate(keys):
        for j, key2 in enumerate(keys):
            if i == j:
                continue
            for k, key3 in enumerate(keys):
                if i == k or j == k:
                    continue
                ans += dic[key1] * dic[key2] * dic[key3]
    print(ans)


if __name__ == '__main__':
    main()
