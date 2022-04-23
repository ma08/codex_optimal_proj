def main():
    num = int(input())
    for i in input().split():
        if int(i) % 2 == 0 and int(i) % 3 != 0 and int(i) % 5 != 0:  # 偶数で3,5の倍数でない
            print("DENIED")
            exit()
    print("APPROVED")

if __name__ == '__main__':
    main()
