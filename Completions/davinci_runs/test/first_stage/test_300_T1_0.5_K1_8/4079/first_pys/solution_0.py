

n = int(input())

for i in range(n):
    s = input()
    check = [False] * 26
    flag = True
    for j in range(len(s) - 1):
        if ord(s[j]) + 1 == ord(s[j + 1]):
            check[ord(s[j]) - ord('a')] = True
            if check[ord(s[j + 1]) - ord('a')]:
                flag = False
                break
        else:
            flag = False
            break
    if flag:
        print('Yes')
    else:
        print('No')