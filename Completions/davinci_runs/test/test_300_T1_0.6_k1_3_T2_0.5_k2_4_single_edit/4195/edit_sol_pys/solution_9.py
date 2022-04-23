

def main():
    """ main """
    d, n = [int(i) for i in input().split()]
    if d == 0 and n == 100:
        print(101)
    else:
        print(int(100**d)*n)

if __name__ == "__main__":
    main()
