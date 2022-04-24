

def main():
    x, y = map(int, input().split())
    if x == y//2 or x == y//2 + 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
