def min_changes(s, t):
    return sum([s[i] != t[i] for i in range(len(t))])

def main():
    s = raw_input()
    t = raw_input()
    print(min_changes(s, t))

if __name__ == '__main__':
    main()
