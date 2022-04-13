
import sys

def main():
    n = int(sys.stdin.readline().strip())
    notes = sys.stdin.readline().strip().split()
    staff = {'G': '', 'F': '', 'E': '', 'D': '', 'C': '', 'B': '', 'A': '', 'g': '', 'f': '', 'e': '', 'd': '', 'c': '', 'b': '', 'a': ''}
    for note in notes:
        if len(note) == 1:
            staff[note] += '*'
        else:
            staff[note[0]] += '*'*int(note[1])
    for line in ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'g', 'f', 'e', 'd', 'c', 'b', 'a']:
        print(line+': '+staff[line])

main()
