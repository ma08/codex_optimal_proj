
def main():
    a, b, k = map(int, input().split())
    x = range(a, b+1)
    x = sorted(x)
    print(*x[:k], sep='\n')
    print(*x[-k:], sep='\n')

if __name__ == '__main__':
    main()
