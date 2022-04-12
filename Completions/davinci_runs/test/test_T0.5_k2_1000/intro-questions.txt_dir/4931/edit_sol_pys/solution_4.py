

def main():
    # read input
    x, y = map(int, input().split())  # read input

    if y == 1:  # if y is 1
        if x == 0:
            print("ALL GOOD")  # if x is 0
        else:
            print("IMPOSSIBLE")
    else:
        print(-x / (y - 1))

if __name__ == "__main__":
    main()
