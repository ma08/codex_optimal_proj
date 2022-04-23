
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
    for i in range(len(keys)):
        for j in range(i+1, len(keys)-1):
            for k in range(j+1, len(keys)-2):
                ans += dic[keys[i]] * dic[keys[j]] * dic[keys[k]] * 6
    print(ans)


if __name__ == '__main__':
    main()
