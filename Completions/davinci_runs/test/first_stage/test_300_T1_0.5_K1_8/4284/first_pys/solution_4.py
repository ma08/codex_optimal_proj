

def main():
    queries = int(input())
    for i in range(queries):
        k, n, a, b = map(int, input().split())
        if k < n*b:
            print(-1)
        else:
            print(k-n*b)

if __name__ == "__main__":
    main()