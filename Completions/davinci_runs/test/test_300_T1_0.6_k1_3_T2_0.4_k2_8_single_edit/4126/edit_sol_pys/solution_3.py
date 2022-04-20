s = input()

if s == s[::-1]:
    if s[:len(s)//2] == s[:len(s)//2][::-1]:
        if s[(len(s)+3)//2-1:] == s[(len(s)+3)//2-1:][::-1] or len(s) == 1:
            print('Yes')
            exit()
print('No')
