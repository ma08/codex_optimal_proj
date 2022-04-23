

def main():
    n = int(input())
    a = [int(i) for i in input().split()]  # a is a list of integers
    d = min(a)  # d is the minimum element in a
    for i in range(n):
        a[i] = a[i] - d
    if sum(a) % n == 0:
        print(d)
    else:
        print(-1)

if __name__ == "__main__":
    main()
