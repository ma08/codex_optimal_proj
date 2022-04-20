

def main():
    a, b, c, d = map(int, input().split())
    if a == c or b == d:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
