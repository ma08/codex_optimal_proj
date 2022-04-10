

def main():
    """main"""
    _ = input()
    t = input()
    ans = 0
    i = 0
    j = 0
    while i < len(t):
        if j == len(t):
            break
        if t[i] == t[j]:
            i += 1
        j += 1
    ans = len(t) - i
    print(ans)

if __name__ == '__main__':
    main()