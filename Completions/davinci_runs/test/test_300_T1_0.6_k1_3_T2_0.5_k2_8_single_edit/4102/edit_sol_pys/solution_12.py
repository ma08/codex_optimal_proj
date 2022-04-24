

def main():
    num = int(input())
    if num:
        while num:
            if num % 10 > (num // 10) % 10:
                print('Yes')
                return 0
            num //= 10
        print('Yes')
    else:
        print('Yes')

main()
