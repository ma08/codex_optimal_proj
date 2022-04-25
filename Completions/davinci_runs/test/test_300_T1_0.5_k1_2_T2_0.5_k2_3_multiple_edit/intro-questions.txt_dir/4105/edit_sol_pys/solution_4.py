
n = int(input())
s = input()
k = int(input())
for i in s:
    if i.isalpha():
        if i.isupper():
            print(chr((ord(i) - ord('A') + k) % 26 + ord('A')), end='')
        else:
            print(chr((ord(i) - ord('a') + k) % 26 + ord('a')), end='')
    else:
        print(i, end='')
