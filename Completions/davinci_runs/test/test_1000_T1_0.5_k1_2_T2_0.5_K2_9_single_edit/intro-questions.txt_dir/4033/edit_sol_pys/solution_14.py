

def main():
    a, b = map(int, input().split())  # read two ints

    if a == b:
        print(4 * a)  # print 4 a
    else:
        print(2 * (a + b))  # print 2 a + 2 b

if __name__ == "__main__":
    main()
