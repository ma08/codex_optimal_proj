

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    max_diff = 0
    for i in range(n):
        for j in range(i+1, n):
            diff = abs(a[i]-a[j])
            if diff > max_diff:
                max_diff = diff
    print(max_diff)

if __name__ == '__main__':
    main()