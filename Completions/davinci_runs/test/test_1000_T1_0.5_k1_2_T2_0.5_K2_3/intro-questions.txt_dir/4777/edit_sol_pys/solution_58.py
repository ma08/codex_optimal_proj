

def main():
    k = int(input())
    x = 0
    y = 1
    for _ in range(k):
        x, y = y, x + y
    print(x, y)

if __name__ == "__main__":
    main()
