

def main():
    a, b = map(int, input().split())

    if a == b: return print(4*a)

    if a < b:
        a, b = b, a

    # a > b
    if (a+b) % 3 == 0: return print(2*(a+b)//3)
    return print(2*(a+b)//3+1)


if __name__ == "__main__":
    main()
