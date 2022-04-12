

def main():
    a, b, c, d = map(int, input().split())
    if a == b or b == c or c == a or d == a or d == b or d == c:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
