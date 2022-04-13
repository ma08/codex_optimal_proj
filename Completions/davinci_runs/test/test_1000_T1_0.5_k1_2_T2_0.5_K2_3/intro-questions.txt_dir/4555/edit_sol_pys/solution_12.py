

def main():
    a, b, k = map(int, input().split())
    x = range(a, b+1)
    print(*sorted(x[:k]), sep='\n')
    print(*sorted(x[-k:]), sep='\n')

if __name__ == '__main__':
    main()
