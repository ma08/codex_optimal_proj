

def main():
    # read input
    n, h, v = [int(x) for x in raw_input().split()]

    # compute largest volume
    volume = (n - max(h, n - h)) * (n - max(v, n - v)) * 4

    # display result
    print(volume)

if __name__ == "__main__":
    main()
