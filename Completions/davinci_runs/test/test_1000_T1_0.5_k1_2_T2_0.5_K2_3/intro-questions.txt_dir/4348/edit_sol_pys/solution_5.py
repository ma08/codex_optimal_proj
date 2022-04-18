
# solution

n, k = map(int, input().split())
s = input()

for i in range(k):
    if 'a' in s:
        s = s[s.find('a')+1:]
    if 'b' in s:
        s = s[s.find('b')+1:]
    if 'c' in s:
        s = s[s.find('c')+1:]
    if 'd' in s:
        s = s[s.find('d')+1:]
    if 'e' in s:
        s = s[s.find('e')+1:]
    if 'f' in s:
        s = s[s.find('f')+1:]
    if 'g' in s:
        s = s[s.find('g')+1:]
    if 'h' in s:
        s = s[s.find('h')+1:]
    if 'i' in s:
        s = s[s.find('i')+1:]
    if 'j' in s:
        s = s[s.find('j')+1:]
    if 'k' in s:
        s = s[s.find('k')+1:]
    if 'l' in s:
        s = s[s.find('l')+1:]
    if 'm' in s:
        s = s[s.find('m')+1:]
    if 'n' in s:
        s = s[s.find('n')+1:]
    if 'o' in s:
        s = s[s.find('o')+1:]
    if 'p' in s:
        s = s[s.find('p')+1:]
    if 'q' in s:
        s = s[s.find('q')+1:]
    if 'r' in s:
        s = s[s.find('r')+1:]
    if 's' in s:
        s = s[s.find('s')+1:]
    if 't' in s:
        s = s[s.find('t')+1:]
    if 'u' in s:
        s = s[s.find('u')+1:]
    if 'v' in s:
        s = s[s.find('v')+1:]
    if 'w' in s:
        s = s[s.find('w')+1:]
    if 'x' in s:
        s = s[s.find('x')+1:]
    if 'y' in s:
        s = s[s.find('y')+1:]
    if 'z' in s:
        s = s[s.find('z')+1:]
print(s)
