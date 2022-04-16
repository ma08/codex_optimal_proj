

def main(n, d, k):
    result = [1]
    for i in range(k):
        result.insert(d[i], len(result) + 1)
    print(" ".join(map(str,result)))

if __name__ == "__main__":
    n = int(input())
    d = list(map(int, input().split(" ")))
    main(n,d)
