

def main():
    """
    N, K = map(int, input().split())
    L = list(map(int, input().split()))

    L.sort(reverse=True)
    print(sum(L[:K]))
    """
    N, K = map(int, input().split())
    L = sorted(map(int, input().split()), reverse=True)
    print(sum(L[:K]))

if __name__ == '__main__':
    main()