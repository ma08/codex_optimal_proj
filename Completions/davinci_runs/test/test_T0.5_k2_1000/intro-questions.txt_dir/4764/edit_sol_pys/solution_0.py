

def main():
    # read input
    n, h, v = [int(x) for x in input().split()]  # type: int

    # compute largest volume
    volume = (n - max(h, n - h)) * (n - max(v, n - v)) * 4  # type: int

    # display result
    print(volume)

if __name__ == "__main__":
    main()
