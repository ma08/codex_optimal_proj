

def main():
    a, b, c, d = map(int, input().split())
    if a == b or b == c or c == d or a == c or a == d or b == d:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
