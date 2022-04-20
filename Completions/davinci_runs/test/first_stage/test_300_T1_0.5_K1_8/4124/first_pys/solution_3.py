

def main():
    s = input()
    t = input()
    count = 0
    while s != '' and t != '':
        if s[0] != t[0]:
            count += 1
        s = s[1:]
        t = t[1:]
    print(len(s) + len(t) + count)

if __name__ == "__main__":
    main()