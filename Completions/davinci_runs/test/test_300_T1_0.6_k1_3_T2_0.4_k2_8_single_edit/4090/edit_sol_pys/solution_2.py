

def main():
    n = int(input())
    words = [w.lower() for w in words]
    words = input().split()
    d = {}
    for i in range(n):
        if words[i] in d:
            d[words[i]] += 1
        else:
            d[words[i]] = 1

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)  # sort by value
    prev = -1
    res = 0
    for i in range(len(d)):
        if d[i][1] != prev:
            res += len(d[i][0])
            prev = d[i][1]
        else:
            res += 1
    print(res)

if __name__ == "__main__":
    main()
