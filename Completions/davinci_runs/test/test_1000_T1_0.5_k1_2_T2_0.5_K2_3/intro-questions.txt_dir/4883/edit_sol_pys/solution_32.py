import sys

def main():
    input = sys.stdin.readline
    m, n = map(int, input().split())
    d = {}
    for _ in range(m):
        a, b = input().split()
        d[a] = b
    for _ in range(n):
        a, b = input().split()
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
