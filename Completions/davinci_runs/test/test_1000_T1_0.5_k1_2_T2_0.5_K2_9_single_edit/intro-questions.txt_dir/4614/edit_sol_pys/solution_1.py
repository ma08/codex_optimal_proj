
def main():
    a, b, c = map(int, input().split())  # a, b, c = [int(i) for i in input().split()]
    if a == b:
        print(c)
    elif a == c:
        print(b)
    else:
        print(a)


if __name__ == "__main__":
    main()
