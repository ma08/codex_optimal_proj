

def main():
    n = int(input())
    words = input().split()
    d = {}
    for i in range(n):
        if words[i] in d:
            d[words[i]] += 1
        else:
            d[words[i]] = 1

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    prev = -1
    res = 0
    for i in range(n):
        if d[i][1] != prev:
            res += len(d[i][0])
            prev = d[i][1]
        else:
            res += 1
    print(res)

if __name__ == "__main__":
    main()
