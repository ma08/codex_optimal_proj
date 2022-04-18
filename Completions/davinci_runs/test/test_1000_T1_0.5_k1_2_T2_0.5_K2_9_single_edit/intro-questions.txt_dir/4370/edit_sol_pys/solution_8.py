

def main():
    a, b = map(int, input().split())
    if a+b <= 16 and a <= 8 and b <= 8:
        if (a+b) % 2 == 0:
            print("Yay!")
        else:
            print(":(")
    else:
        print(":(")

if __name__ == "__main__":
    main()
