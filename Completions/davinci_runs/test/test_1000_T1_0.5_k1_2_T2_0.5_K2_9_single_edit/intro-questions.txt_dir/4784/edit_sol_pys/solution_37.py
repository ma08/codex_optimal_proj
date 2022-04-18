

def main():
    x = int(input())
    n = int(input())
    megabytes = x
    for i in range(n):
        megabytes = megabytes - int(input())
    print(megabytes)


if __name__ == '__main__':
    main()
