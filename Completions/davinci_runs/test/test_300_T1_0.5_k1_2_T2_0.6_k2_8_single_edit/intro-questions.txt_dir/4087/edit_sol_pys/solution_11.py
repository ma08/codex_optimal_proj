

def main():
    n = int(input())
    while True:
        if n % 4 == 0:
            print(n)
            break
        else:
            n += 1

if __name__ == '__main__':
    main()
