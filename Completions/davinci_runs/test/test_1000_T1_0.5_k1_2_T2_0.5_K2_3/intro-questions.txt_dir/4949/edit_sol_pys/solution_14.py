

def main():
    n, w, h = map(int, input().split())
    for i in range(n):
        match = int(input())
        if match <= w or match <= h or match ** 2 <= w ** 2 + h ** 2:  # Pythagorean theorem
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
