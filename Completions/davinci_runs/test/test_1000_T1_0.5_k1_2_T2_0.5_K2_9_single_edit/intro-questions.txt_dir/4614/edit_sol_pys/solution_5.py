
def main():
    a, b, c = map(int, input().split(" "))
    if a == b:
        print(c, end=" ")
    elif a == c:
        print(b, end=" ")
    else:
        print(a, end=" ")

if __name__ == '__main__':
    main()
