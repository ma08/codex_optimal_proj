

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 2 == 0:
            print(n//2)
        else:
            print(n//2 + 1)

if __name__ == '__main__':
    main()
