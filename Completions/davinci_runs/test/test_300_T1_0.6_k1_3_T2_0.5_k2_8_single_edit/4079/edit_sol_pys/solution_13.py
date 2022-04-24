

def main():
    n = int(input())
    for i in range(n):
        string = input()
        if len(string) == len(set(string)):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
