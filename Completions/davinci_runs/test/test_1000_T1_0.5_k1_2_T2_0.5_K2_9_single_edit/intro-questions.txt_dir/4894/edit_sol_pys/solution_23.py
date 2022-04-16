

import sys

def main():
    n = int(sys.stdin.readline().strip())
    notes = sys.stdin.readline().strip().split()
    lines = [l.strip() for l in sys.stdin.readlines()]
    staff = []
    for line in lines:
        staff.append(line.split())
    for note in notes:
        if len(note) == 1:
            staff[ord(note.lower()) - ord('a')].append('*') # ord('a')=97
        else:
            staff[ord(note[0].lower()) - ord('a')].append('*' * int(note[1])) # ord('a')=97
    for line in staff:
        print(' '.join(line))

main()
