

def main():
    n = int(input())
    doublets_count = 1
    for _ in range(n):
        d1, d2 = map(int, input().split())
        doublets_count = doublets_count + 1 if d1 == d2 else 0
        if doublets_count == 3: break
    print('Yes' if doublets_count == 3 else 'No')

if __name__ == '__main__':
    main()
