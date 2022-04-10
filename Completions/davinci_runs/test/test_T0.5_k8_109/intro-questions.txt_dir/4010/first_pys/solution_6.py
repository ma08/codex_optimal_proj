

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        for j in range(n):
            for k in range(j+1, n):
                if a[j] == a[k]:
                    for l in range(k+1, n):
                        if a[l] == a[j]:
                            print("YES")
                            break
                    else:
                        print("NO")
                    break
            else:
                continue
            break
        else:
            print("NO")

if __name__ == "__main__":
    main()