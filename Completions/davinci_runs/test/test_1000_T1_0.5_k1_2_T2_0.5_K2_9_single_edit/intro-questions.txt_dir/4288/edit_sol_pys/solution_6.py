

def main():
    a, b, c = map(int, input().split())
    if a == b or b == c or a == c or a + b == c or b + c == a or a + c == b:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
