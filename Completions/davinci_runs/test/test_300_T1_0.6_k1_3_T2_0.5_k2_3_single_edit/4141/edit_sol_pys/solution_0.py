

def main():
    num = int(input())
    for i in range(num):
        if int(input()) % 2 == 0 and int(input()) % 3 != 0 and int(input()) % 5 != 0:
            print("DENIED")
            exit()
    print("APPROVED")

if __name__ == '__main__':
    main()
