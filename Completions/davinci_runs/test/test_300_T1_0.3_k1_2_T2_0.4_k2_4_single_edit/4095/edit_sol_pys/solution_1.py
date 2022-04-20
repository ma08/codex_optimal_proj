

def main():
    n, m = map(int, input().split())  # n is the number of elements in the array, m is the number of elements to be counted
    p = list(map(int, input().split()))
    count = 0  # count the number of subarrays
    for i in range(n):
        for j in range(i, n):
            if p[i:j+1].count(m) > 0:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
