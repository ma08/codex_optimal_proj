
from sys import stdin

def main():
    n = int(stdin.readline().strip())
    notes = stdin.readline().strip().split()
    staff = {'G':'', 'F':'', 'E':'', 'D':'', 'C':'', 'B':'', 'A':'', 'g':'', 'f':'', 'e':'', 'd':'', 'c':'', 'b':'', 'a':''}
    for note in notes:
        if len(note) == 1:
            staff[note] += '*'
        else:
            staff[note[0]] += '*'*int(note[1])
    for l in ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'g', 'f', 'e', 'd', 'c', 'b', 'a']:
        print(l+': '+staff[l])

main()
