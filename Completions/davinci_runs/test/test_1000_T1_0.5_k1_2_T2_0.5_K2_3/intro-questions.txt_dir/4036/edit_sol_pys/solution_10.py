def main():
    n, k = map(int, input().split())
    # n = number of people
    # k = number of groups
    if(n == 1 and k == 1):
        print("YES")
        print("1")
    elif(n < k):
        print("NO")
    elif(n >= k):
        a = [1]
        for i in range(1, k):
            a.append(2 * a[i - 1])
        if(sum(a) <= n):
            print("YES")
            print(" ".join(map(str, a)))
        else:
            print("NO")
    else:
        print("NO")

if __name__ == "__main__":
    main()
