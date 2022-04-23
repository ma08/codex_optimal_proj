

def count_change(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            count += 1
    return count


def main():
    s = input()
    print(count_change(s))


if __name__ == '__main__':
    main()
