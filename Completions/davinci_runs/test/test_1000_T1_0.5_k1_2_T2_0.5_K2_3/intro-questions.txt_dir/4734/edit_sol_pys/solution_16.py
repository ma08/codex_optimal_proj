

def main():
    s = input().split()
    result = []
    for word in s:
        if word.endswith(('ex', 'ix')):
            result.append(word)
        elif word.endswith(('e', 'i')):
            result.append(word[:-1] + 'x')
        elif word.endswith(('a', 'i', 'o', 'u')):
            result.append(word[:-1] + 'ex')
        else:
            result.append(word + 'ex')
    print(*result)

if __name__ == "__main__":
    main()
