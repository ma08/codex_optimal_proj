
def main():
    n, k = map(int, input().split())
    if(n == 1 and k == 1):
        print("YES")
        print("1")
    elif(n < k):
        print("NO")
    elif(n > k and n % 2 == 0):
        a = [1]
        for i in range(k - 1):
            a.append(2 * a[i])
        if(sum(a) == n):
            print("YES")
            print(" ".join(map(str, a)))
        else:
            print("NO")
        elif(n > k and n % 2 == 1):
            a = [1]
            for i in range(k - 2):
                a.append(2 * a[i])
            a.append(n - sum(a))
            if(sum(a) == n):
                print("YES")
                print(" ".join(map(str, a)))
            else:
                print("NO")

if __name__ == "__main__":
    main()
