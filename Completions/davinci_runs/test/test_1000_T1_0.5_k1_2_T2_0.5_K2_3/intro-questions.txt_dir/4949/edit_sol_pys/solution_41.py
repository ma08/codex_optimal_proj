

def main():
    n, w, h = map(int, input().split())
    for i in range(n):
        match_ = int(input())
        if match_ <= w or match_ <= h or match_ ** 2 <= w ** 2 + h ** 2: 
            print("DA")
        else:
            print("NE")

if __name__ == "__main__":
    main()
