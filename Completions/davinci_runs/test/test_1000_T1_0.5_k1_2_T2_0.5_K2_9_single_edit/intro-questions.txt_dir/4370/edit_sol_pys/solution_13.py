

def main():
    a, b = map(int, input().split())
    if a+b <= 16:  # add a and b
        if (a+b) % 2 == 0:
            print("Yay!")  # if even
        else:
            print(":(")  # if odd
    else:
        print(":(")  # if greater than 16

if __name__ == "__main__":
    main()
