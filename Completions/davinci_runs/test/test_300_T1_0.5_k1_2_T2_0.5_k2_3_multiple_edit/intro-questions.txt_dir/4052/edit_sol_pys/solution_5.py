

def main():
    # read data for n sequences
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    t = []
    for i in range(n):
        t.append(input())

    # solve
    for i in range(n):
        if s[i] == t[i]:
            print(0)
        else:
            # create a dictionary to store the number of occurrences of each character
            d = {}
            for j in range(len(s[i])):
                if s[i][j] in d:
                    d[s[i][j]] += 1
                else:
                    d[s[i][j]] = 1
                if t[i][j] in d:
                    d[t[i][j]] -= 1
                else:
                    d[t[i][j]] = -1
            flag = True
            for key in d:
                if d[key] != 0:
                    flag = False
                    break
            if flag:
                k = 0
                l = 0
                count = 0
                while k < len(s[i]) and l < len(t[i]):
                    if s[i][k] == t[i][l]:
                        k += 1
                        l += 1
                    else:
                        k += 1
                        count += 1
                if count > 10000:
                    print(-1)
                else:
                    print(count)
                    k = 0
                    l = 0
                    while k < len(s[i]) and l < len(t[i]):
                        if s[i][k] == t[i][l]:
                            k += 1
                            l += 1
                        else:
                            print(k, end=' ')
                            k += 1
                            count += 1
            else:
                print(-1)
                if i != n - 1:
                    i += 1

main()
