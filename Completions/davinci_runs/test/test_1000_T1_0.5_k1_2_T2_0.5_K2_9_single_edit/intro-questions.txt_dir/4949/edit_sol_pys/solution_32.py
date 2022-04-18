
def main():
    n, w, h = map(int, input().split())
    for i in range(n):
        match = input()
        if int(match) <= w or int(match) <= h or int(match) ** 2 <= w ** 2 + h ** 2:
            print("DA")
        else:
            print("NE")

if __name__ == "__main__":
    main()
