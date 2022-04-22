

def min_changes(s, t):
    count = 0
    for i in range(len(s)):
        if len(t) > i:
            if s[i] != t[i]:
                count += 1
        else:
            count += 1


    return count

def main():
    s = input()
    t = input()
    print(min_changes(s, t))

if __name__ == '__main__':
    main()
