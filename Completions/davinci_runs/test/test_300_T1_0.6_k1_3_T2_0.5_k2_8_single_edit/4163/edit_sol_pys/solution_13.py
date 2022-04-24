

def main():
    n = int(input())
    doublets_count = 0
    for i in range(n):
        doublet = map(int, input().split())
        if doublet[0] == doublet[1]:
            doublets_count += 1
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
