

def main():
    s = input()
    count = 0
    if s[0] == '0':
        count += 1
    if s[-1] == '0':
        count += 1
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()