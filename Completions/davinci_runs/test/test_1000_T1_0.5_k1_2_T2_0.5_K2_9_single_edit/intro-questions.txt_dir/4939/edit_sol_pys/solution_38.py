

def pangram(string, alphabet):
    for i in alphabet:
        if i not in string:
            return False
    return True

print(pangram("The quick brown fox jumps over the lazy dog", "abcdefghijklmnopqrstuvwxyz"))
