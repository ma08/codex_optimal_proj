

def main():
    n = int(input())
    arr = [int(s) for s in input().split()]
    res = find_blocks(arr)
    print(len(res))
    for l, r in res:
        print(l+1, r+1)

if __name__ == "__main__":
    main()
