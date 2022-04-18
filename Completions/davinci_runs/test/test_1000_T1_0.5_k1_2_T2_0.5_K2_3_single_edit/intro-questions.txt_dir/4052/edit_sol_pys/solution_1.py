

def main():
    # read data for n sequences
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i = input()
        s.append(s_i)
        t_i = input()
        t.append(t_i)

    # solve
    for i in range(n):
        if s[i] == t[i]:
            print(0)
        else:
            # create a dictionary to store the number of occurences of each character
            d = {}
            for j in range(n):
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
                j = 0
                k = 0
                count = 0
                while j < n and k < n:
                    if s[i][j] == t[i][k]:
                        j += 1
                        k += 1
                    else:
                        j += 1
                        count += 1
                if count > 10000:
                    print(-1)
                else:
                    print(count)
                    j = 0
                    k = 0
                    while j < n and k < n:
                        if s[i][j] == t[i][k]:
                            j += 1
                            k += 1
                        else:
                            print(j, end=' ')
                            j += 1
                            count += 1
            else:
                print(-1)

main()
