

def main():
    n = int(input())
    m = n
    while m % 2 != 0:
        m += n
    print(m)

if __name__ == '__main__':
    main()