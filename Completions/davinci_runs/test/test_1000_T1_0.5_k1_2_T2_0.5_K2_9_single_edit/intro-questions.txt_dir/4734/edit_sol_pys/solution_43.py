

def main():
    word, pos = input().split()
    if word.endswith('ex'):
        print(word + pos)
    elif word.endswith('e'):
        print(word[:-1] + 'x' + pos)
    elif word.endswith(('a', 'i', 'o', 'u')):
        print(word[:-1] + 'ex' + pos)
    else:
        print(word + 'ex' + pos)

if __name__ == "__main__":
    main()
