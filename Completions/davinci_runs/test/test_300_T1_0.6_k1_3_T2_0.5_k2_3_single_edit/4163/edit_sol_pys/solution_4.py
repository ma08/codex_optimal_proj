

def main():
    n = int(input())
    doublets_count = 1
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 <= d2:
            doublets_count += 1
        else:
            doublets_count = 0
        if doublets_count == 4:
            break
    if doublets_count == 4:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
