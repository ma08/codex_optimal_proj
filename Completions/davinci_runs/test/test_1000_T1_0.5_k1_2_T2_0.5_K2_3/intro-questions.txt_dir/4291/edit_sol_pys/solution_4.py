

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        ans += 1/i
    print(1/ans) 

if __name__ == '__main__':
    main()
