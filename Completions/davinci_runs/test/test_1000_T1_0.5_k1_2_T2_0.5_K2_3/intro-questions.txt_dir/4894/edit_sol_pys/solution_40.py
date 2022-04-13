

import sys

def main():
    n = int(sys.stdin.readline().strip())
    notes = sys.stdin.readline().strip().split()
    lines = [l.strip() for l in sys.stdin.readlines()]
    staff = [] # [['*'], ['*'], ['*'], ['*'], ['*'], ['*'], ['*'], ['*']]
    for line in lines:
        staff.append(list(line))
    for note in notes: # a3
        if len(note) == 1: # a
            staff[ord(note.lower()) - ord('a')].append('*')
        else:
            staff[ord(note[0].lower()) - ord('a')].extend(['*'] * int(note[1]))
    for line in staff:
        print(' '.join(line))

main()
