
n = int(input())

def main():
    while True:
        n += 1
        if n % sum([int(i) for i in str(n)]) == 0:
            print(n)
            break

if __name__ == '__main__':
    main()
