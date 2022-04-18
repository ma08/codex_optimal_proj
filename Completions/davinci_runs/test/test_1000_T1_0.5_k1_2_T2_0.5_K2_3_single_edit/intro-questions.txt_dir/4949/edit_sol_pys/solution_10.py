

def main():
    n, w, h = map(int, input().split())
    for i in range(n):
        match = int(input())
        if match <= w or match <= h or match * match <= w * w + h * h:
            print("DA")
        else:
            print("NE")

if __name__ == "__main__":
    main()
