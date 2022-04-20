

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))[::-1]
    for i in range(k):
        a[i] = 0
    print(sum(a))

if __name__ == '__main__':
    main()
