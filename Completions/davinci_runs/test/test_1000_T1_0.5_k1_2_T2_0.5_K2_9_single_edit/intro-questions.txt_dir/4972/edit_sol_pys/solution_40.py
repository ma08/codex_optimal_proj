

def main():
    """main function"""
    num = int(input())
    k = 0
    while num > 1:
        k += 1
        num = num // (2*k + 1)
    print(k)

if __name__ == "__main__":
    main()
