

def main():
    a = int(input())
    if a % 4 == 0:
        print(a)
    else:
        while True:
            a += 1
            if a % 4 == 0:
                print(a)
                break

if __name__ == '__main__':
    main()
