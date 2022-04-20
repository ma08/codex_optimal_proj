

def main():
    n = int(input())
    a = input()
    if a == a[::-1]:
        print("wins")
    else:
        print("losses")

if __name__ == "__main__":
    main()
