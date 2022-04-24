

def main():
    num = int(input())
    for i in range(num):
        for j in input().split():
            if int(j) % 2 == 0 and int(j) % 3 != 0 and int(j) % 5 != 0:
                print("DENIED")
                exit()
        print("APPROVED")

if __name__ == '__main__':
    main()
