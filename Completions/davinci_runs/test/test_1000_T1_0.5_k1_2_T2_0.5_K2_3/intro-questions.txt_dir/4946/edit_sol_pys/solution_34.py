

def main():
    n = int(input())
    langs = list(map(int, input().split(' ')))
    d = {}
    for i in range(n):
        if langs[i] not in d:
            d[langs[i]] = [i]
        else:
            d[langs[i]].append(i)
    min_dist = n+1
    for key in d:
        lst = d[key]
        for i in range(len(lst)-1):
            min_dist = min(min_dist, lst[i+1]-lst[i])
    print(min_dist)

if __name__ == '__main__':
    main()
