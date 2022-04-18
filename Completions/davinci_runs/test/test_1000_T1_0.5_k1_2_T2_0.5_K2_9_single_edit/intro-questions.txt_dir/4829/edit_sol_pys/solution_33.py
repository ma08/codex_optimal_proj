

def main():
    l,r = map(int,input().split())
    if l==r:
        print(f"Even {l+r}")
    elif l>r:
        print(f"Odd {2*l}")
    elif l<r:
        print(f"Odd {2*r}")
    else:
        print("Not a moose")

if __name__ == '__main__':
    main()
