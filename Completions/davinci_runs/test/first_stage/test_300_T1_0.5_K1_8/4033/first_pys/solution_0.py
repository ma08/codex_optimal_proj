

def main():
    """
    a + b = (x * y)
    x = a + b - y
    y = a + b - x
    """
    a, b = map(int, input().split())
    x, y = a, b
    if x > y:
        x, y = y, x
    while x > 0:
        if a + b - y < x:
            x -= 1
            y += 1
        else:
            break
    print((x + y) * 2)

if __name__ == "__main__":
    main()