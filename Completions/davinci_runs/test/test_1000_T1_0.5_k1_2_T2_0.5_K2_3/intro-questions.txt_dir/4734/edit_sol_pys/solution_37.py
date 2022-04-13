

def main():
    word, post = input().split(' ')
    if word.endswith('ex'):
        print(word + ' ' + post)
    elif word.endswith('e'):
        print(word[:-1] + 'x ' + post)
    elif word.endswith(('a', 'i', 'o', 'u')):
        print(word[:-1] + 'ex ' + post)
    else:
        print(word + 'ex ' + post)

if __name__ == "__main__":
    main()
