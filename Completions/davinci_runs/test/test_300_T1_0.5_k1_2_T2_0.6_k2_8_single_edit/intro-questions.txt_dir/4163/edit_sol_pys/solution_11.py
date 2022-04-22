

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print('Yes' if a.count(5) == 2 and a.count(7) == 1 else 'No')

if __name__ == '__main__':
    main()
