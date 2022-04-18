

def main():
    a, b, c = map(str, input().split())
    if a == b or b == c or a == c:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
