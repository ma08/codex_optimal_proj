import sys

s = input()
try:
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')
except:
    print('usage: python3 pluar.py <word>')
