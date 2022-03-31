

def main():
    """
    This is pretty much a brute force solution. 
    """
    n = int(input())
    m = set()
    for i in range(1, n + 1):
        m.add(i)
        while i % 10 == 0:
            i //= 10
    print(len(m))


if __name__ == "__main__":
    main()
