

def main():
    N, K = map(int, input().split())
    L = sorted(map(int, input().split()))
    print(sum(L[:K]))

if __name__ == '__main__':
    main()
