

def main():
    l, r = map(int, input().split(' '))
    if l == r:
        print("Even {}".format(l + r))
    elif l > r:
        print("Odd {}".format(2 * l))
    else:
        print("Odd {}".format(2 * r))

if __name__ == "__main__":
    main()
