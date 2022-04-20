

def main():
    a, b, c = map(int, input().split())
    if a == b or b == c or a == c or a + b + c == 21:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
