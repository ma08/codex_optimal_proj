

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_num = max(a)
    min_num = min(a)
    if max_num == min_num:
        print('YES')
        return
    if max_num - min_num > 1:
        print('NO')
        return
    if a.count(max_num) > 1 and a.count(min_num) > 1:
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    main()
