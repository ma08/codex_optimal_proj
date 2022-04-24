

def main():
    N = int(input())

    if N % 4 == 0 or N % 4 == 3:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
