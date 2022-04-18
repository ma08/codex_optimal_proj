
def main():
    n, k = map(int, input().split())
    if(n == 1 and k == 1):
        print("yes")
        print("1")
    elif(n < k or n > k):
        print("no")
    elif(n > k):
        a = [1]
        for i in range(k - 1):
            a.append(2 * a[i])
        if(sum(a) == n):
            print("yes")
            print(" ".join(map(str, a)))
        else:
            print("no")
    else:
        print("no")

if __name__ == "__main__":
    main()
