

def min_changes(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            j += 1
        else:
            i += 1
            j += 1
    return len(t) - j

def main():
    s = input()
    t = input()
    print(min_changes(s, t))

if __name__ == '__main__':
    main()
