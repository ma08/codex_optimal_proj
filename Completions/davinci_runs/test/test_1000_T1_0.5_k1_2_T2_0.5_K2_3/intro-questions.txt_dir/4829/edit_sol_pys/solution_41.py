

def main():
    l,r = map(int,input().split())
    if l==r:
        print("Even {}".format(l+r))
    elif l>r:
        print("Odd {}".format(2*l)
    elif l<r:
        print("Odd {}".format(2*r)
    else:
        print("Not a moose")

if __name__ == '__main__':
    main()
