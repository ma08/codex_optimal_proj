
def min_changes(s, t):
    count = 0
    for i in range(len(s)):
        if s[i] != t[i] and i < len(t):
            count += 1
    return count

def main():
    s = input()
    t = input()
    print(min_changes(s, t))

if __name__ == '__main__':
    main()
