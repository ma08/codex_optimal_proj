

def main():
    a, b, c, d = map(int, input().split())
    print("Yes" if a + b == c + d or a + c == b + d or a + d == b + c else "No")

if __name__ == "__main__":
    main()
