

def main():
    n = input()
    if len(n) == 1:
        print("Yes")
        return
    if n == n[::-1]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
