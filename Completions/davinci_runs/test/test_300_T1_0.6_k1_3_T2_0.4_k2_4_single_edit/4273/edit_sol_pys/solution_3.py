

def main():
    N, A, B = map(int, input().split())
    ans = 0
    for i in range(N+1):
        s = sum([int(j) for j in str(i)])
        if A <= s <= B:
            ans += i
    print(ans)

if __name__ == '__main__':
    main()
