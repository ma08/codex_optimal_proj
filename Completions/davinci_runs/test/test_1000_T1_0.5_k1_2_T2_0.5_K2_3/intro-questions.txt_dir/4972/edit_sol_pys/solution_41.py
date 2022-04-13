

def main():
    """main function"""
    n = int(input())
    k = 0
    while n > 1:
        k += 1
        n = n // (2*k + 1)
    print(k)

if __name__ == "__main__":
    main()
