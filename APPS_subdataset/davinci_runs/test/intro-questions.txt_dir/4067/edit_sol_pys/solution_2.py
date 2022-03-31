

def main():
    n = int(input())
    s = input()
    s = list(s)
    s.sort(reverse=True)
    ans = []
    i = 0
    while i < len(s):
        if s[i] == '0':
            ans.append(s[i])
            i+=1
        elif s[i] == '1':
            ans.append(s[i])
            i+=1
        else:
            ans.append(s[i])
            i+=1
            ans.append(s[i])
            i+=1
            ans.append(s[i])
            i+=1
    print(''.join(map(str, ans)))

if __name__ == '__main__':
    main()
