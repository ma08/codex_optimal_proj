

def main():
    n = int(input())
    d = 1
    p = 1
    while p < n:
        p *= 2
        d += 1
    print(d)

if __name__ == "__main__":
    main()
