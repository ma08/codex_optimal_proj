

def main():
    # read data for n sequences
    n = int(input())
    s = list(input())
    t = list(input())

    # solve
    if s == t or n == 1:
        print(0)
    else:
        # create a dictionary to store the number of occurences of each character
        d = {}
        for i in range(n-1):
            if s[i+1] in d:
                d[s[i+1]] += 1
            else:
                d[s[i+1]] = 1
            if t[i+1] in d:
                d[t[i+1]] -= 1
            else:
                d[t[i+1]] = -1
        flag = True
        for key in d:
            if d[key] != 0:
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
                i = 0
                j = 0
                while i < n and j < n:
                    if s[i] == t[j]:
                        i += 1
                        j += 1
                    else:
                        print(i, end=' ')
                        i += 1
                        count += 1
        else:
            print(-1)

main()
