
import sys

def main(argv):
    n = int(sys.stdin.readline().strip())
    notes = sys.stdin.readline().strip().split()
    lines = [l.strip() for l in sys.stdin.readlines()]
    staff = []
    for line in lines:
        staff.append(line.split()) # split each line
    for note in notes:
        if len(note) == 1: # if note is single
            staff[ord(note.lower()) - ord('a')].append('*')
        else: # if note is double
            staff[ord(note[0].lower()) - ord('a')].append('*' * int(note[1]))
    for line in staff: # print staff
        print(' '.join(line))

if __name__ == "__main__":
    main(sys.argv)
