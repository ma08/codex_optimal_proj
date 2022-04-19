

def main():
    a, b, c, d = map(int, input().split())
    if a == b or b == c or a == c or c == d or b == d or a == d:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
