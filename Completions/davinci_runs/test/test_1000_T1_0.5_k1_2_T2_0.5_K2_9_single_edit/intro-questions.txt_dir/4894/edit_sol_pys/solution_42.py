

import sys

def main():
    n = int(sys.stdin.readline().strip())
    notes = sys.stdin.readline().strip().split()
    staff = {'G':'', 'F':'', 'E':'', 'D':'', 'C':'', 'B':'', 'A':'', 'g':'', 'f':'', 'e':'', 'd':'', 'c':'', 'b':'', 'a':''} # create dictionary
    for note in notes:
        if len(note) == 1: # if note is a single character
            staff[note] += '*' # add a star to the key in the dictionary
        else:
            staff[note[0]] += '*'*int(note[1])
    for l in ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'g', 'f', 'e', 'd', 'c', 'b', 'a']:
        print(l+': '+staff[l])

main()
