
def main():
    s = input()
    t = input()
    out = []
    for i in range(int(len(s)/2)):
        if s[2*i] != t[i]:
            out.append(s[2*i])
        if s[2*i+1] != t[i]:
            out.append(s[i])
    print("".join(out))


if __name__ == '__main__':
    main()
