

def main():
    k = int(input())
    x, y = 0, 1
    for i in range(k):
        x, y = y, x + y
    print(x, y)

if __name__ == "__main__":
    main()
