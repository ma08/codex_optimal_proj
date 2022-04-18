

def main():
    n = int(input()) #input the number
    if n == 1:
        print(1)
    else:
        print(n + (n - 1) // 9)

if __name__ == "__main__":
    main()
