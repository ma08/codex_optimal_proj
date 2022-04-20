
def main():
    n, k = map(int, input().split())
    if(n == 1 and k == 1):
        print("YES")
        print("1", end="")
    elif(n < k):
        print("NO")
        print("1", end="")
    elif(n > k):
        a = [1]
        for i in range(k - 1):
            a.append(2 * a[i])
        if(sum(a) == n):
            print("YES")
            print(" ".join(map(str, a)), end="")
        else:
            print("NO")
            print("1", end="")
    else:
        print("NO")
        print("1", end="")

if __name__ == "__main__":
    main()
