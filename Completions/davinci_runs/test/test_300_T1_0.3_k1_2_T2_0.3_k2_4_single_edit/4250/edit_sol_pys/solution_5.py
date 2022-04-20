
import sys

def main():
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    d = {i: s.count(i) for i in s}
    t = sorted(d.keys(), key=lambda x: d[x], reverse=True)[:k]
    print(' '.join(map(str, t)))

if __name__ == '__main__':
    main()
