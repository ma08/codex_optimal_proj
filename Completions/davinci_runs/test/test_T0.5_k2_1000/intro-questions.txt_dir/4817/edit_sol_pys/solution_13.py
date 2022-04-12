

def main():
    # Read input
    x = input()

    j = len(x) - 1
    while x[j] <= x[i - 1]:
        j -= 1
    x[i - 1], x[j] = x[j], x[i - 1]

    x[i:] = reversed(x[i:])
    return True

if __name__ == "__main__":
    main()
