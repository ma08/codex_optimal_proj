

def main():
    """ main """
    x, y = [int(i) for i in input().split()]
    if x == 0:
        print(y)
    else:
        print(100*y)

if __name__ == "__main__":
    main()
