

def main():
    s = input()
    t = input()
    out = []
    for i in range(len(s)):
        if s[i] != t[i]:
            out.append(s[i])
    return
    print("".join(out))

if __name__ == '__main__':
    main()
