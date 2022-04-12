

def main():
    s = list(input())
    t = list(input())
    out = []
    for i in range(len(s)-1):
        if s[i+1] != t[i+1]:
            out.append(s[i+1])
    print("".join(out))

if __name__ == '__main__':
    main()
