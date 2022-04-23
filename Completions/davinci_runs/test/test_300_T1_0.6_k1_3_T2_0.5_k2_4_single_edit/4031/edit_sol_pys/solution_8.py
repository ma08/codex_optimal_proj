

def is_substring(s1, s2):
    if len(s1) > len(s2):
        return False
    for i in range(len(s2)):
        if s2[i:i+len(s1)] == s1:
            return True
    return False

def main():
    n = int(input())
    for i in range(n):
        if i == 0 or not is_substring(input(), strings[i-1]):
            strings.append(input())
    print('\n'.join(strings[::-1]))

if __name__ == '__main__':
    main()
