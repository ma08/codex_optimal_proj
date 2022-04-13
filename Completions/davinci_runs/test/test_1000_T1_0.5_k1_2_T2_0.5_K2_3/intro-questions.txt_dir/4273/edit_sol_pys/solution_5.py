
import sys

def main():
    n = int(sys.stdin.readline())
    names = [sys.stdin.readline().strip() for _ in range(n)]
    dic = {}
    for name in names:
        if name[0] in dic:
            dic[name[0]] += 1
        else:
            dic[name[0]] = 1
    keys = list(dic.keys())
    ans = 0
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            for k in range(j+1, len(keys)):
                ans += dic[keys[i]] * dic[keys[j]] * dic[keys[k]]
    print(ans)


if __name__ == '__main__':
    main()
