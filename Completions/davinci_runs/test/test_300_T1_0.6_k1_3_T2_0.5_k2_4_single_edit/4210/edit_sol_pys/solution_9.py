

def main():
    n, k = map(int, input().split())  # n: number of elements, k: divisor
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):  # i: index of the first element
        for j in range(i+1, n):  # j: index of the second element
            if i == j:
                continue
            num = int(str(a[i]) + str(a[j]))
            if num % k == 0:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
