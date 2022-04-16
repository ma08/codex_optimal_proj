

def main():
    with open('input.txt', 'r') as f:
        n = int(input())
        a = [int(s) for s in input().split()]
        res = find_blocks(a)
        print(len(res))
        for l, r in res:
            print(l+1, r+1)

    with open('output.txt', 'w') as f:
        print(len(res), file=f)
        for l, r in res:
            print(l+1, r+1, file=f)

if __name__ == "__main__":
    main()
