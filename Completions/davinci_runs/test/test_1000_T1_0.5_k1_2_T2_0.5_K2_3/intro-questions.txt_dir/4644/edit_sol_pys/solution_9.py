
def main():
    t = int(input())  # no. of test cases
    for _ in range(t):
        n = int(input())  # no. of elements in array
        a = list(map(int, input().split()))
        if sum(a) % 2 == 0:
            print("NO")
        else:
            print("YES")


if __name__ == '__main__':
    main()
