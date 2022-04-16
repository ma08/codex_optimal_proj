

def main():
    r, g, b = map(int, input().split())
    num = r * 100 + g * 10 + b
    if num % 4 == 0: # 条件分岐はif, elif, else
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
