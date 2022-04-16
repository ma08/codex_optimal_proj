

def main():
    s = input()
    t = input()
    out = []
    for i in range(0, len(s), 2):
        if s[i:i+2] != t[i:i+2]:
            out.append(s[i:i+2])
    print("".join(out))

if __name__ == '__main__':
    main()
