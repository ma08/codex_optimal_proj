
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if 0 in a:
            break
        else:
            a = list(map(lambda x: x / 2, a))
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
