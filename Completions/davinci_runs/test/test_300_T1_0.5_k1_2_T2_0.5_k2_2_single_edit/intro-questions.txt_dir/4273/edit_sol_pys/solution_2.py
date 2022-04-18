
import sys

def main():
    n = int(sys.stdin.readline())
    name = [sys.stdin.readline().strip() for _ in range(n)]
    d = {}
    for i in name:
        if i[0] in d:
            d[i[0]] += 1
        elif i[0] not in d:
            d[i[0]] = 1
    key = d.keys()
    a = 0
    for j in range(len(key)):
        for k in range(j+1, len(key)):
            for l in range(k+1, len(key)):
                a += d[key[j]] * d[key[k]] * d[key[l]]
    print(a)


if __name__ == '__main__':
    main()
