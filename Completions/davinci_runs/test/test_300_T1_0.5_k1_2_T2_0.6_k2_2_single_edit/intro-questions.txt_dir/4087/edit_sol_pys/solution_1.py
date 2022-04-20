

def main():
    a = int(input())
    while True:
        if a % 4 == 0 and a % 100 != 0:
            break
        elif a % 400 == 0:
            print("Високосный")
            print(a)
            break
        else:
            a += 1

if __name__ == '__main__':
    main()
