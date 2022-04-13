def main():
    l, r = map(int, input().split())
    if l == r:
        print("Even " + str(l + r))
    elif l > r:
        print("Odd " + str(2 * l))
    else:
        print("Odd " + str(2 * r))

if __name__ == "__main__":
    main()
