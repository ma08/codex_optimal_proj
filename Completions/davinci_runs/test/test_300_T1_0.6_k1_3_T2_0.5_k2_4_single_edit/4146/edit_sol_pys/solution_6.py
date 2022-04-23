

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}
    for i in range(n):
        if a[i] in d.keys():
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    print(d)

if __name__ == '__main__':
    main()
