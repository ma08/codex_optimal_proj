

def main():
    # Read input and convert to integer
    x = int(input())
    y = int(input())

    if y == 1:
        print("ALL GOOD")
    else:
        print(-x / (y - 1))

if __name__ == "__main__":
    main()
