

def main():
    n = int(input())
    a = list(map(int, input().split()))  # read the input
    # if 2 consecutive numbers are equal, increase both by 1
    for i in range(n-1):
        if a[i] == a[i+1]:
            a[i] += 1
    # if all numbers are equal, they are all even
            a[i+1] += 1
    if len(set(a)) == 1:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
