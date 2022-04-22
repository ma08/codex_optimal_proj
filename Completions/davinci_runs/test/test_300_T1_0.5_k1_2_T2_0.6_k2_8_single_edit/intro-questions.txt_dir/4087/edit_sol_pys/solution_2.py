

def main():
    num = int(input())
    while True:
        if num % 4 == 0:
            print(num)
            break
        else:
            num += 1

if __name__ == '__main__':
    main()
