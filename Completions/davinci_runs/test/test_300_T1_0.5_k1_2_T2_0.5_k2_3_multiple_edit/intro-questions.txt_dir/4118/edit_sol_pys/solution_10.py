
def main():
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x > 20 or x < 1 or y > 20 or y < 1:
        print(-1)
        return
    print(x * y)

if __name__ == '__main__':
    main()
