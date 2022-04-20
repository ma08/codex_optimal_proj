

def main():
    n = input()
    if len(n) % 2 == 0:
        print("No")
    else:
        if n[0] == n[-1]:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
