

def get_min_packages(n, k):
    if k == 1:
        return n
    else:
        return 1 + get_min_packages(n-k, k-1)

def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        print(get_min_packages(n, k))

if __name__ == '__main__':
    main()