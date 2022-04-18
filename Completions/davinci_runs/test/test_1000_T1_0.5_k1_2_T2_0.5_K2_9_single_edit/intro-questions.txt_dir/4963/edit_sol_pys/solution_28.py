

def main():
    n = int(input())
    d = list(map(int, input().split(" ")))
    result = [0] * len(d)
    for i in range(len(d)):
        result[d[i]-1] = i + 1
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
