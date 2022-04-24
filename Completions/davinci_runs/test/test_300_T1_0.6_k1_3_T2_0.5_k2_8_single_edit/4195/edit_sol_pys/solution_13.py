

def main():
    """ main """
    d, n = [int(i) for i in input().split()] # d = 0 or 1, n = integer
    if d == 0:
    elif d == 1:
        print(100*n)
        print(n)
    else:
        print(10000*n)

if __name__ == "__main__":
    main()
