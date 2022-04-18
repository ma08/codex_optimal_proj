

def main():
    a, b = map(int, input().split())

    if a == 1:
        if b == 2:
            print(3)
        else:
            print(2)
    elif a == 2:
        if b == 1:
            print(3)
        else:
            print(1)
    else:
        if b == 1:
            print(2)
        else:
            print(1)

if __name__ == "__main__":
    main()
