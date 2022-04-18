
#s = input()
#vowels = ['a', 'e', 'i', 'o', 'u']
#new_s = ''

#i = 0
#while i < len(s):
#    if s[i] in vowels:
#        new_s += s[i]
#        i += 2
#    else:
#        new_s += s[i]
#        i += 1

#print(new_s)

def foo(x):
    return x + 1

def bar(x):
    return x + '1'

print(bar(foo(1)))
