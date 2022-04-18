
import sys

def main(argv):
    n = int(sys.stdin.readline().strip())
    notes = sys.stdin.readline().strip().split()
    lines = [l.strip() for l in sys.stdin.readlines()][:5]
    staff = []
    staff_letters = 'abcde'
    for line in lines:
        staff.append(line.split()[:n])
    for note in notes:
        if len(note) == 1:
            staff[ord(note.lower()) - ord('a')][0] = '*'
        else:
            staff[ord(note[0].lower()) - ord('a')][0] = '*' * int(note[1])
    for line in staff:
        print(' '.join(line))

if __name__ == "__main__":
    main(sys.argv)
