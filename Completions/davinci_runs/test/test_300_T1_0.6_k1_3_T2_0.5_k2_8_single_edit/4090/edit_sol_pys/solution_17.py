

    words = input().split()
def main():
    n = int(input())
    d = {}
    for i in range(n):
        d[words[i]] = d.get(words[i], 0) + 1

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    res = 0
    for i in range(len(d)):
        res += len(d[i][0])
    print(res)

if __name__ == "__main__":
    main()
