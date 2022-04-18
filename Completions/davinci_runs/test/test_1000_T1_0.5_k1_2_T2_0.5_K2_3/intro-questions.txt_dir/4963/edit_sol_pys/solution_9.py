

def main(n, d):
    result = [1]
    for i in d:
        result.insert(i, len(result) + 1)
    print(*result)

if __name__ == "__main__":
    n = int(input())
    d = list(map(int, input().split(" ")))
    main(n, d)
