

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(sum(a[::2]))

if __name__ == '__main__':
    main()
