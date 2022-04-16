import sys

def main():
    n = int(sys.stdin.readline().strip())
    notes = sys.stdin.readline().strip()
    notes = notes.split()
    octave = {'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'a': 'A', 'b': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'A': 'A', 'B': 'B'}
    staff = {'C': 'C: ', 'D': 'D: ', 'E': 'E: ', 'F': 'F: ', 'G': 'G: ', 'A': 'A: ', 'B': 'B: '}    
    for x in range(0, n):
        if len(notes[x]) == 1:
            if notes[x].islower():
                staff[octave[notes[x]]] += '*'
            else:
                staff[octave[notes[x].lower()]] += '*'
        else:
            if notes[x][0].islower():
                staff[octave[notes[x][0]]] += '*'*int(notes[x][1])
            else:
                staff[octave[notes[x][0].lower()]] += '*'*int(notes[x][1])
    for x in range(0, len(staff['C'])):
        for y in staff.keys():
            if x < len(staff[y]):
                print(staff[y][x], end='')
            else:
                print(' ', end='')
        print()

main()
