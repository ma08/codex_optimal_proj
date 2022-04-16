

def main():
    n = int(input())
    d = 0
    while n > 1:
        n //= 2
        d += 1
    print(d + 1)

if __name__ == "__main__":
    main()
