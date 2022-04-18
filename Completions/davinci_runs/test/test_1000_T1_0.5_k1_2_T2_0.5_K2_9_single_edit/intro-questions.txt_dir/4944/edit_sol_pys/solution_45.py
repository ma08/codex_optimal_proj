def main():
    n = int(input())
    d = 0
    p = 1
    while p < n:
        p *= 2
        d += 1
    print(d + 1)

if __name__ == "__main__":
    main()
