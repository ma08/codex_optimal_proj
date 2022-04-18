

word = input().split()

if word[-1] == 'e':
    print(word + 'x' + p)
elif word[-1] in 'aiou':
    print(word[:-1] + 'ex' + p)
elif word[-2:] == 'ex':
    print(word + p)
