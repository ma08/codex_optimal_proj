

def main():
    n, k = map(int, input().split())  # n, k = (int(i) for i in input().split())
    a = list(map(int, input().split()))
    print(sum(1 for i in a if i <= k))

if __name__ == '__main__':
    main()
