

def main():
    a = int(input())
    while True:
        if a % 4 == 0 and a % 100 != 0:
            print(a)
        elif a % 400 == 0:
            print(a)
            break
            break
        else:
    print("That's it")
            a += 1

if __name__ == '__main__':
    main()
