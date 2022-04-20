

def min_changes(s, t, k):
    if k < abs(len(s) - len(t)):
        return -1
    else:
        count = 0
        for i in range(len(t)):
            if s[i] != t[i]:
                count += 1
        return count

def main():
    s = input()
    t = input()
    k = int(input())
    print(min_changes(s, t, k))

if __name__ == '__main__':
    main()
