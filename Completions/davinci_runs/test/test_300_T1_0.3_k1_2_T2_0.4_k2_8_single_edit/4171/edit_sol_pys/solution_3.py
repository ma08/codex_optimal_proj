

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    print(max(a) - min(a) - 1)

if __name__ == '__main__':
    main()
