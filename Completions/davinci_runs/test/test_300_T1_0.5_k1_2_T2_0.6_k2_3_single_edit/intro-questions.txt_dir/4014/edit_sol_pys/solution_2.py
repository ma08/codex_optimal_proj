

def main():
    n = int(input())
    s = input()
    
    ans = [0] * n
    
    for i in range(n):
        if s[i] == '?':
            if i > 0:
                if s[i - 1] == 'a':
                    ans[i] = 'b'
                elif s[i - 1] == 'b':
                    ans[i] = 'a'
                else:
                    ans[i] = 'a'
            else:
                ans[i] = 'a'
        else:
            ans[i] = s[i]
    
    for i in range(1, n):
        if ans[i] == ans[i-1]:
            print('-1')
            return
    print(''.join(ans))

if __name__ == "__main__":
    main()
    
