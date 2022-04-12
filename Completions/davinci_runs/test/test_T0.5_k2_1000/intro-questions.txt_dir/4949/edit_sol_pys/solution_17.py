

def main():
    n, w, h = map(int, input().split())
    for i in range(n):
        match = int(input())
        if match <= w or match <= h or match ** 2 <= w ** 2 + h ** 2:
            print("DA")
        else:
            print("NE")

if __name__ == "__main__":
    main()
