

def main():
    n = int(input())
    s = input()
    print("YES")
    for i in range(n-1):
        if s[i] != s[i+1]:
            print("1", end="")
        else:
            print("0", end="")
    print(0)


if __name__ == "__main__":
    main()