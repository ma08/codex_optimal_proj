


def main():
    l, r = map(int, input().split())
    if l == 0 and r == 0:
        print("Not a moose") 
    else:
        if l == r:
            print("Even {}".format(2*l))
        else:
            print("Odd {}".format(2*max(l, r)))

if __name__ == "__main__":
    main()
