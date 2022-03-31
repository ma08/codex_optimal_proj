

#Solution

n = int(input())
s = input()
t = input()

if s == t:
    print(0)
else:
    ans = []
    for i in range(n):
        if s[i] == t[i]:
            continue
        for j in range(i + 1, n):
            if s[j] == t[i]:
                ans.append(j)
                s = s[:j] + s[j+1:] + s[j]
                break
        else:
            print(-1)
            break
    else:
        print(len(ans))
        print(*ans)