
def main():
    n, k = map(int, input().split())  # n is number of elements and k is the number of queries
    s = input()  # string
    cost = 0
    for i in range(n):
        if s[i] == '1':
            cost += i + 1
        else:
            cost += min(i + 1, n - i)
    print(cost)

if __name__ == "__main__":
    main()
