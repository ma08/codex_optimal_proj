

def main():
    n = int(input())
    s = input()
    ans = ['0' for x in range(n)] # array of 0s
    flag = 0
    for i in range(n-1):
        if (s[i] > s[i+1]):
            if (flag == 1):
                print("NO")
                return
            else:
                ans[i] = '1' # change 0 to 1
                ans[i+1] = '0' # change 1 to 0
                flag = 1
    print("YES")
    print(''.join(ans))

main()
