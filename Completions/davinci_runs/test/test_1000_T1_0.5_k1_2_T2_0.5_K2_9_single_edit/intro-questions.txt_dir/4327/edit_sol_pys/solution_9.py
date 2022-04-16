
def main():
    # a, p = map(int, input().split())
    # print(p // 2 + (a + p % 2) * 3 // 2)
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    count = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if x == 500 * i + 100 * j + 50 * k:
                    count += 1
    print(count)




if __name__ == '__main__':
    main()
