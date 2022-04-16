
def main():
    # Read input
    n, h, v = [int(x) for x in input().split()]

    # Compute largest volume
    volume = (n - max(h, n - h)) * (n - max(v, n - v)) * 4

    # Display result
    print(volume)

if __name__ == "__main__":
    main()
