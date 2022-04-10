
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if n % 2 == 0:
        if a[0] == a[n**2//2-1]:
            print("YES")
            for i in range(n):
                print(" ".join([str(x) for x in a[i*n:(i+1)*n]]))
        else:
            print("NO")
    else:
        if a[0] == a[(n//2)*(n+1)-1]:
            print("YES")
            for i in range(n):
                if i < n//2:
                    print(" ".join([str(x) for x in a[i*n:(i+1)*n]]))
                elif i == n//2:
                    print(a[(n//2)*(n+1)-1])
                else:
                    print(" ".join([str(x) for x in a[i*n:i*n+n//2][::-1]]), end="")
        else:
            print("NO")

main()
