

def main():
    l, r = map(int, input().split())
    if l == r:
        print("Even %d" % (l + r), end='')
    elif l > r:
        print("Odd %d" % (2 * l), end='')
    else:
        print("Odd %d" % (2 * r), end='')

if __name__ == "__main__":
    main()
