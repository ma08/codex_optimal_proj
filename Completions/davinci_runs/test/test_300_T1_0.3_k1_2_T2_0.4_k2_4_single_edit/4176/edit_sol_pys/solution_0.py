
def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    ans = a
    while ans % b != 0:
        ans += a
    print(ans)

if __name__ == "__main__":
    main()
