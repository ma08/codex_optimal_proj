import sys

def main():
    n = int(sys.stdin.readline())
    langs = list(map(int, sys.stdin.readline().split()))
    d = {}
    for i in range(n):
        if langs[i] not in d:
            d[langs[i]] = [i]
        else:
            d[langs[i]].append(i)
    min_dist = n
    for key in d:
        l = d[key]
        for i in range(len(l)-1):
            min_dist = min(min_dist, l[i+1]-l[i])
    sys.stdout.write(str(min_dist))

if __name__ == '__main__':
    main()
