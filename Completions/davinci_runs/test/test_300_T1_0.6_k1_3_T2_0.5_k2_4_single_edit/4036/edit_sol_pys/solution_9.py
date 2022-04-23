

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    # print(a)
    # print(len(a))
    # print(sum(a))
    # print(sum(a) % n)
    if sum(a) % n == 0:
        print(n)
    else:
        print(n - 1)

if __name__ == "__main__":
    main()
































