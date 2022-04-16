

word,post = input().split()

if word[-1]=='e':
    print(word+'x'+post)
elif word[-1] in ['a','i','o','u']:
    print(word[:-1]+'ex'+post)
elif word[-2:]=='ex':
    print(word+post)
