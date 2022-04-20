

def main():
    n = input()
    if len(n) == 1 or n[0] == n[-1]:
        print("Yes")  # return
    else:
        print("No")

if __name__ == "__main__":
    main()
