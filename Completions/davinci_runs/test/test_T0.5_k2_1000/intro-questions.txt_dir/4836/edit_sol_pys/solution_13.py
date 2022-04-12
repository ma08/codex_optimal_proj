
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum(1 for x in a if x < k))

if __name__ == "__main__":
    main()
