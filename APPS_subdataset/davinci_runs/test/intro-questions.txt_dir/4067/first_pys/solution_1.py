

def main():
    n = int(input())
    s = input()
    s = list(map(int, s))
    s.sort()
    ans = []
    a = 0
    b = 1
    c = 2
    i = 0
    while i < len(s):
        if s[i] == 0:
            ans.append(s[i])
            i+=1
        elif s[i] == 1:
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