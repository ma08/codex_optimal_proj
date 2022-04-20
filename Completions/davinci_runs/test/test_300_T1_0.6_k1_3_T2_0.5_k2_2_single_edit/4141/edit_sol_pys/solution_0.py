
def main():
    num = int(input())
    for i in input().split():
        if int(i) % 2 != 0 or int(i) % 3 == 0 or int(i) % 5 == 0:
            print("DENIED")
            exit()
    print("APPROVED")

if __name__ == '__main__':
    main()
