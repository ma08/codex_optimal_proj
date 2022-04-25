

def find_occurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def main():
    s = input()
    a = find_occurences(s, 'a')
    b = find_occurences(s, 'b')
    c = find_occurences(s, 'c')
    if len(a) > 0 and len(b) > 0 and len(c) > 0:
        print('Yes')
        return
    else:
        print('No')

main()
