
def main():
    words = input().split()
    seen = set()
    for word in words:
        if word in seen:
            print('No')
            return
        seen.add(word)
    print('Yes')

if __name__ == '__main__':
    main()
