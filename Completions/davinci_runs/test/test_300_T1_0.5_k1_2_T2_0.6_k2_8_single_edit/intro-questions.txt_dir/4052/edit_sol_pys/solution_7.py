

def main():
    # read data for n sequences
    n = int(input())
    s = input()
    t = input()

    # solve
    if s == t:
        print(0)
    else:
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

main()
