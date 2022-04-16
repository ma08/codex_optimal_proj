

def main():
    l, r = map(int, input().split())
    if l == r:
        print("Even %d" % (l + r))
    else:
        print("Odd %d" % (2 * l))

if __name__ == "__main__":
    main()
