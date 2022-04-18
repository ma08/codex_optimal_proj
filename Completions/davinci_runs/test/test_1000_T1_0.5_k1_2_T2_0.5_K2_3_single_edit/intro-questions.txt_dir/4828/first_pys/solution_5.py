

def main():
    #n = int(input())
    #for i in range(n):
    #    print(i)
    #    print(input())
    #    print("")
    #return

    #s = input()
    #print(s)
    #return

    s = input()
    n = 0
    for i in range(len(s)):
        if (i % 4 == 0) and (s[i].isupper()):
            pass
        else:
            n += 1
    print(n)
    return


if __name__ == "__main__":
    main()