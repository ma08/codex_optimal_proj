

def main():
    """ main """
    d, n = [int(i) for i in input().split()]
    if d == 0:
        print(n)
    else:
        print(100*n if d == 1 else 10000*n)

if __name__ == "__main__":
    main()
