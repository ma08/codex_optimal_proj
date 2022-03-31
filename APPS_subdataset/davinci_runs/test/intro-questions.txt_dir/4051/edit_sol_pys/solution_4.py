
def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = [0 for i in range(101)]  # 0 to 100
    for i in a:
        l[i] += 1
    for i in range(1, 101):
        l[i] += l[i - 1]
    for i in range(100, 0, -1):  # shift right
        l[i] = l[i - 1]
    l[0] = 0
    for i in range(1, 101):
        l[i] += i
    if l[-1] == n:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
