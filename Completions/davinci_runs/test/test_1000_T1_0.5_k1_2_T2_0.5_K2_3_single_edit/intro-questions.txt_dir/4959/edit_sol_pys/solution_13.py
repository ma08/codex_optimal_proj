

def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    print(s[n//2] - s[n//2-1])

if __name__ == '__main__':
    main()
