
def min_changes(s, t, n):
    count = 0
    for i in range(n):
        if s[i] != t[i]:
            count += 1
    return count

def main():
    s = input()
    t = input()
    print(min_changes(s, t, len(t)))

if __name__ == '__main__':
    main()
