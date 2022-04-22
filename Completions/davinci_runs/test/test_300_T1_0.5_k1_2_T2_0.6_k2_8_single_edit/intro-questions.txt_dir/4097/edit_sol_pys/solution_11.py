

def main():
    a, b = map(int, input().split())
    if a == b:
        print("EQUAL")
    elif a == b * 2:
        print("DOUBLE")
    elif a * 2 == b:
        print("HALF")
    elif a > b:
        print("GREATER")
    elif a < b:
        print("LESS")

if __name__ == '__main__':
    main()
