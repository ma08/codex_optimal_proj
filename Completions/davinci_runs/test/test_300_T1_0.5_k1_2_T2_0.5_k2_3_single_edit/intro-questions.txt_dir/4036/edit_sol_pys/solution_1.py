
def main():
    n, k = map(int, input().split())
    if(n == 1 and k == 1):
        print("Yes")
        print("1")
    elif(n < k):
        print("No")
    elif(n > k):
        a = [1]
        for i in range(k - 1):
            a.append(2 * a[i])
        if(sum(a) == n):
            print("Yes")
            print(" ".join(map(str, a)))
        else:
            print("No")
    else:
        print("No")

if __name__ == "__main__":
    main()
