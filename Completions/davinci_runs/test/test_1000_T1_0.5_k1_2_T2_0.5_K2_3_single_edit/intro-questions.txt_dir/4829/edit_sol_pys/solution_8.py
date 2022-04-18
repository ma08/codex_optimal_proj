

def main():
    a, b = map(int, input().split())
    if a == b:
        print("Even %d" % (a + b))
    elif a > b:
        print("Odd %d" % (2 * a))
    else:
        print("Odd %d" % (2 * b))

if __name__ == "__main__":
    main()
