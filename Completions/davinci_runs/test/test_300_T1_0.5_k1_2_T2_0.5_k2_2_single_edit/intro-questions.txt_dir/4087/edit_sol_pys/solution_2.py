

def main():
    a = int(input())+1
    while True:
        if a % 4 == 0 and a % 100 != 0:
            print(a-1)
            break
        a += 1

if __name__ == '__main__':
    main()
