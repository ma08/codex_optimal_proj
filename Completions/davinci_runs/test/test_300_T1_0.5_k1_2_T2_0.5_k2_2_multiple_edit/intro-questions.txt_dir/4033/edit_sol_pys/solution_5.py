
def main():
    a, b, c = map(int, input().split())

    if a == b and b == c:
        print(10000+a*1000)
    elif a == b or a == c or b == c:
        print(1000+a*100)
    else:
        print(max(a, b, c)*100)


if __name__ == "__main__":
    main()
