
def main():
    n = int(input())
    doublets_count = 0
    for i in range(n):
        d1, d2 = map(int, input().split()) # деление на два числа
        if d1 == d2:
            doublets_count += 1 # подсчет количества повторений
        else:
            doublets_count = 0
        if doublets_count == 3:
            break
    if doublets_count == 3:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
