

def main():
    # read data for n sequences
    n = int(input())
    s = list(input())
    t = list(input())

    # solve
    if s == t:
        print(0)
    else:
        # create a dictionary to store the number of occurrences of each character
        d = {}
        for i in range(n):
            if s[i] not in d:
                d[s[i]] = 0
            d[s[i]] += 1
            if t[i] not in d:
                d[t[i]] = 0
            else:
                d[t[i]] += 1
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
                if s[i] != t[j]:
                    count += 1
                    j += 1
                else:
                    i += 1
                    j += 1
            if count > 10000:
                print(-1)
            else:
                print(count)
                j = 0
                for i in range(n):
                    if s[i] != t[j]:
                        print(i + 1, end=' ')
                    else:
                        j += 1
        else:
            print(-1)

main()
