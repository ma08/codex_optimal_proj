
def min_changes(s, t, n, m):
    count = 0
    for i in range(n):
        if s[i] != t[i]:
            count += 1

    return count

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    print(min_changes(s, t, n, m))

if __name__ == '__main__':
    main()
