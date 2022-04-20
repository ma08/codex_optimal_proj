

def main():
    l, r = map(int, input().split())
    ans = float('inf')
    for i in range(l, r):
        for j in range(i+1, r+1):
            ans = min(ans, i*j%2019)
    print(ans)

if __name__ == '__main__':
    main()