

def main():
    n = int(input())
    lang = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if lang[i] not in d:
            d[lang[i]] = [i]
        else:
            d[lang[i]].append(i)
    min_dist = n
    for key in d:
        l = d[key]
        for i in range(len(l)-1):
            min_dist = min(min_dist, l[i+1]-l[i])
    print(min_dist)

if __name__ == '__main__':
    main()
