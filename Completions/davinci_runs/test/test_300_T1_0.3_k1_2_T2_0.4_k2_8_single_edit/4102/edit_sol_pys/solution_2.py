

def main():
    n = input()
    if len(n) == 1:
        print("Yes")
        return
    for i in range(len(n) // 2):
        if n[i] != n[-i - 1]:
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()
