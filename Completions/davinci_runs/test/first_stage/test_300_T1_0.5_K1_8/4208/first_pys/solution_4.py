

import sys

def color_pairs(l, r):
    l_indices = {}
    for i, c in enumerate(l):
        l_indices.setdefault(c, []).append(i)
    pairs = []
    for i, c in enumerate(r):
        if c == '?':
            for j in l_indices.get('?', []):
                pairs.append((j, i))
        else:
            for j in l_indices.get(c, []):
                pairs.append((j, i))
    return len(pairs), pairs


def main():
    n = int(sys.stdin.readline())
    l = sys.stdin.readline().strip()
    r = sys.stdin.readline().strip()
    k, pairs = color_pairs(l, r)
    print(k)
    for p in pairs:
        print('{} {}'.format(p[0]+1, p[1]+1))


if __name__ == '__main__':
    main()