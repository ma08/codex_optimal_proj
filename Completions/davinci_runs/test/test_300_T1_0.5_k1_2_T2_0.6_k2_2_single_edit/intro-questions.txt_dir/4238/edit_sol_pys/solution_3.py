

def main():
    N = input()

    if sum(map(int, N)) % 9 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
