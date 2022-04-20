

def main():
    t = int(input())
    while t:
        n = int(input())
        if n == 1:
            print(0)
        else:
            print(n//2)
        t -= 1

if __name__ == '__main__':
    main()