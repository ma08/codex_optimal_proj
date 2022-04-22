
import collections
import sys

def main():
    s = input().rstrip()
    t = input().rstrip()
    if len(s) != len(t):
        print('No')
        return
    d = collections.defaultdict(int)
    for c in s:
        d[c] += 1
    for c in t:
        d[c] -= 1
    for v in d.values():
        if v != 0:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()
