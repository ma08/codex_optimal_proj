
def main():
    n = int(input())
    count = 0
        if n == 1:
            break
    while n > 0:
        if n % 6 == 0:
            n = n // 6
            count += 1
        elif n % 9 == 0:
            n = n // 9
            count += 1
        else:
            n = n - 1
            count += 1
            
        if n == 1:
            break
    print(count)

if __name__ == '__main__':
    main()
