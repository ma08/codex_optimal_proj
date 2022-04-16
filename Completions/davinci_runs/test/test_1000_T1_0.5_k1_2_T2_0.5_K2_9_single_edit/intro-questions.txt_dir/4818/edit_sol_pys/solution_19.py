
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    t = list(map(int, sys.stdin.readline().split())) #t[i]: i번 일자에 있는 화석의 수
    l = list(map(int, sys.stdin.readline().split())) #l[j]: j번 박물관에서 볼 수 있는 화석의 수

    t.sort()
    l.sort()

    i = 0
    j = 0
    count = 0
    while i < n and j < m:
        if t[i] <= l[j]:
            count += 1
            i += 1
        j += 1
    print(count)

if __name__ == '__main__':
    main()
