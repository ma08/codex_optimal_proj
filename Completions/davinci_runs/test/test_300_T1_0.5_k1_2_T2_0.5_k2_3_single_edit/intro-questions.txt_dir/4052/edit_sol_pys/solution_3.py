

def main():
    # read data for n sequences
    n = int(input())
    s = input()
    t = input()

    # solve
    if s == t or n == 1:
        print(0)
    else:
        # create a dictionary to store the number of occurences of each character
        d = {}
        for i in range(n):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            if t[i] in d:
                d[t[i]] -= 1
            else:
                d[t[i]] = -1
        flag = True
        for i in range(26):
            if d.get(chr(ord('a') + i), 0) != 0:
                flag = False
                break
        if flag:
            i = 0
            j = 0
            count = 0
            while i < n and j < n:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
                    count += 1
            if count > 10000:
                print(-1)
            else:
                print(count)
                print(*indices)
        else:
            print(-1)

main()
