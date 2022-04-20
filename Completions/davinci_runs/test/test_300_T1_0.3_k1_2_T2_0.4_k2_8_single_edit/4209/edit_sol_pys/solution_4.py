

def main():
    x = int(input())
    if x == 1:
        print('YES')
        return
    for i in range(2, x):
        if x % i == 0:
            print('NO')
            return
    print('YES')

if __name__ == '__main__':
    main()
