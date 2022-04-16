

def main():
    n = int(input())
    d = 0
    m = 1
    while m < n:
        m *= 2
        d += 1
    print(d + 1)

if __name__ == "__main__":
    main()
