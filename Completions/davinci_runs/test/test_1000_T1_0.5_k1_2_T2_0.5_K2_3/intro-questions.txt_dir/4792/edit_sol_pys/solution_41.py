
from itertools import groupby

name = input('Enter your name: ')

compact = ''.join([k for k, g in groupby(name)])

print(f'{name} compacted is: {compact}')
