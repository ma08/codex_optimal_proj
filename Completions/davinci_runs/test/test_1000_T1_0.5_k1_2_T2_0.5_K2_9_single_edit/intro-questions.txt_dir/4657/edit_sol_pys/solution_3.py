

def check(n, k, a):
    summ = sum(a)
    if summ % 2 == 0:
        return False
    else:
        return True

def print_out(n, k, a):
    if k == 1:
        print(n)
    elif k == n:
        for i in range(n):
            print(i+1, end = " ")
        print()
    else:
        for i in range(1, n):
            if a[i] % 2 != 0:
                print(i, end = " ")
                for j in range(2, k+1):
                    print(n-j+2, end = " ")
                print()
                break

if __name__ == "__main__":
    q = int(input())

    for i in range(q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        #print(a)

        if k > n:
            print("NO")
            continue

        if check(n, k, a):
            print("YES")
            print_out(n, k, a)
        else:
            print("NO")
