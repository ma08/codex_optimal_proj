

def is_diverse(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = [letter for letter in string]
    letters = ''.join(sorted(set(letters)))
    if len(letters) == 1:
        return True
    elif len(letters) == 2:
        if letters in alphabet:
            return True
        else:
            return False
    else:
        for i in range(len(letters)-1):
            if letters[i+1] != alphabet[alphabet.index(letters[i])+1]:
                return False
        return True

def main():
    n = int(input())
    for _ in range(n):
        string = input()
        if is_diverse(string):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()