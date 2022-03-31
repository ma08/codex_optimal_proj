

def main():
    n,k = [int(x) for x in input().strip().split()]
    if n%2 == 0:
        print("YES")
        for i in range(1,n+1):
            if i%2 == 0:
                print(i//2,i//2)
            else:
                print(i//2+1,i//2+1)
    else:
        print("YES")
        for i in range(1,n+1):
            if i%2 == 0:
                print(i//2,i//2)
            else:
                print(i//2+1,i//2)
        print(n,n)

if __name__ == '__main__':
    main()