

def main():
    n = int(input())
    seq = [int(x) for x in input().split()]
    if n == 1:
        print(0)
        return
    if n == 2:
        print(1)
        return
    diff = seq[1] - seq[0]
    for i in range(1, n):
        if seq[i] - seq[i-1] != diff:
            print(-1)
            return
    print(1)

if __name__ == "__main__":
    main()
