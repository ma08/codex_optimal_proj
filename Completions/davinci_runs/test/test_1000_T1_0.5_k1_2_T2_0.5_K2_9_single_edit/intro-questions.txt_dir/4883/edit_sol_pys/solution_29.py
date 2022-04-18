
import sys

def main():
    inp = sys.stdin.readline
    m, n = map(int, inp().split())
    d = dict()
    for _ in range(m):
        a, b = inp().split()
        d[a] = b
    for _ in range(n):
        a, b = inp().split()
        if len(a) != len(b):
            print('no')
            continue
        flag = True
        for i in range(len(a)):
            if a[i] not in d or b[i] not in d or d[a[i]] != b[i]:
                flag = False
                break
        if flag:
            print('yes')
        else:
            print('no')

if __name__ == "__main__":
    main()
