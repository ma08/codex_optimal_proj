
def main():
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a + b == 15:
            ans += 1
    print(ans)




if __name__ == '__main__':
    main()
