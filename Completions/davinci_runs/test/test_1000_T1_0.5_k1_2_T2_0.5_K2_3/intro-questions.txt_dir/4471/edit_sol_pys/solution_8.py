

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if n == 1:
            if a[0] == 1:
                print("NO")
            else:
                print("YES")
            continue
        ans = "YES"
        for idx, val in enumerate(a):
            if val == 1:
                if idx == 0:
                    if a[1] == 1:
                        ans = "NO"
                        break
                elif idx == n-1:
                    ans = "YES"
                    break
                else:
                    if a[idx-1] == 1 or a[idx+1] == 1:
                        ans = "NO"
                        break
            elif val == 2:
                if idx == 0:
                    if a[1] == 2:
                        ans = "NO"
                        break
                elif idx == n-1:
                    ans = "NO"
                    break
                else:
                    if a[idx-1] == 2 or a[idx+1] == 2:
                        ans = "NO"
                        break
            elif val == 3:
                if idx == 0:
                    if a[1] == 3:
                        ans = "NO"
                        break
                elif idx == n-1:
                    ans = "YES"
                    break
                else:
                    if a[idx-1] == 3 or a[idx+1] == 3:
                        ans = "NO"
                        break
        print(ans)

if __name__ == "__main__":
    main()
