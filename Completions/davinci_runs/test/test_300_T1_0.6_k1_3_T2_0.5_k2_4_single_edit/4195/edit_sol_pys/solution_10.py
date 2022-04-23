

def main():
    """ main """
    d, n = [int(i) for i in input().split()]
    if d == 0:
        print(n)
    else:
        if n == 100:
            print((100**d)*(n+1))
        else:
            print((100**d)*n)

if __name__ == "__main__":
    main()
