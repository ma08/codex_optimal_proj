
def main():
    l, r = map(int, input().split())
    if l == r:
        print("Even", l + r)
    elif l > r:
        print("Odd", 2 * l)
    else:
        print("Odd", 2 * r)

if __name__ == "__main__":
    main()
