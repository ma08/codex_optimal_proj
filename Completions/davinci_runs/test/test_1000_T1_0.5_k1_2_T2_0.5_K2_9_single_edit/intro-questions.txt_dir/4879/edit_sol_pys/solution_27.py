

def main():
    a, b, c = map(int, input().split())
    if b == a + 1 and c == b + 1:
        print("Yes")
    elif b == a - 1 and c == b - 1:
        print("Yes")
    elif b == a + 1 and c == b - 1:
        print("Yes")
    elif b == a - 1 and c == b + 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
