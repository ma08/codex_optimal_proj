

def main():
    words = input().split() # split words by space
    seen = set()
    for word in words:
        if word in seen:
            print('no')
            return
        seen.add(word)
    print('yes')

if __name__ == '__main__':
    main()
