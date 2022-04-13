

def main(n, m):
    result = [1]
    for i in m:
        result.insert(i, len(result) + 1)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    n = int(input())
    m = list(map(int, input().split(" ")))
    main(n, m)
