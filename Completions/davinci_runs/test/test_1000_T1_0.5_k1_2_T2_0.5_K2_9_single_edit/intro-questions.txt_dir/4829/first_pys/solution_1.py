

def main():
    l, r = map(int, input().split())
    if l == r:
        print("Even %d" % (l + r))
    elif l > r:
        print("Odd %d" % (2 * l))
    else:
        print("Odd %d" % (2 * r))

if __name__ == "__main__":
    main()