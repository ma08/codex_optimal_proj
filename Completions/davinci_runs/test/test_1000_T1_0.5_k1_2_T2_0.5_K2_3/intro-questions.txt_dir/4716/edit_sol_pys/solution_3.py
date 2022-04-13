

def main():
    """
    N, K = map(int, input().split())
    L = list(map(int, input().split()))

    L.sort(reverse=True)
    print(sum(L[:K]))
    """
    N, K = map(int, input().split())  # N: number of items, K: the top K items
    L = sorted(map(int, input().split()), reverse=True)  # list
    print(sum(L[:K]))  # sum of the top K items

if __name__ == '__main__':
    main()
