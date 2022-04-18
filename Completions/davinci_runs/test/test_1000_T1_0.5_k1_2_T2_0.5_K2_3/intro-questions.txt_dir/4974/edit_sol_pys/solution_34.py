
# THIS IS A COMMENT

def main():
    r, n = map(int, input().split())  # split input into two integers
    booked = set()
    for _ in range(n):  # _ is a dummy variable that can be used when you don't need the index
        booked.add(int(input()))
    for i in range(1, r+1):  # range(1, r+1) == [1, 2, 3, ..., r]
        if i not in booked:
            print(i)
            return
    print("too late")

if __name__ == "__main__":
    main()
