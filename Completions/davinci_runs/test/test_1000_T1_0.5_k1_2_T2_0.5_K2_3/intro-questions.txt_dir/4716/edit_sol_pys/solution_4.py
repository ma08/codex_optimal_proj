

def main():
    N, K = map(int, input().split())
    L = sorted(list(map(int, input().split())), reverse=True)
    print(sum(L[:K]))

if __name__ == '__main__':
    main()
