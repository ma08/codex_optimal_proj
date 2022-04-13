
def main():
    # Read the input
    x, y = map(float, input().split())

    if y == 1:
        if x == 0:
            print("ALL GOOD")
        else:
            print("IMPOSSIBLE")
    else:
        print(-x / (y - 1), end="")

if __name__ == "__main__":
    main()
