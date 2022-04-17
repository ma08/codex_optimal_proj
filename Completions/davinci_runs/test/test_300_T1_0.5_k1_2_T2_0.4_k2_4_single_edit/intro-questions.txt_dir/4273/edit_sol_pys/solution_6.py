import sys


def main():
    N = int(sys.stdin.readline())
    names = [sys.stdin.readline().strip() for _ in range(N)]
    dic = dict()
    for name in names:
        if name[0] in dic:
            dic[name[0]] += 1
        else:
            dic[name[0]] = 1
    keys = list(dic.keys())
    ans = 0
    for i in range(len(keys)-2):
        for j in range(i+1, len(keys)-1):
            for k in range(j+1, len(keys)): # O(N^3)
                ans += dic[keys[i]] * dic[keys[j]] * dic[keys[k]]
    print(ans)

if __name__ == '__main__':
    main()
