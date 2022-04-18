

def main(n, d):
    result = []
    for i in d:
        result.insert(i - 1, len(result) + 1)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    n = int(input())
    d = list(map(int, input().split(" ")))
    main(n, d)
