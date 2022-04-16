

def main():
    n = int(input())
    langs = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if langs[i] not in d:
            d[langs[i]] = [i+1]
        else:
            d[langs[i]].append(i+1)
    min_dist = n
    for key in d:
        l = d[key]
        for i in range(1, len(l)):
            min_dist = min(min_dist, l[i]-l[i-1])
    print(min_dist)

if __name__ == '__main__':
    main()
