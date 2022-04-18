
import sys

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

def main():
    n = int(sys.stdin.readline().strip())
    song = sys.stdin.readline().strip().split()
    song = [notes.index(x) for x in song] # convert to numbers
    scales = []
    for i in range(12):
        if valid(i, song): # check if scale is valid
            scales.append(i)
    if len(scales) == 0:
        print("none")
    else:
        print(' '.join([notes[x] for x in scales])) # convert back to letters

def valid(i, song):
    scale = [i, (i+2)%12, (i+4)%12, (i+5)%12, (i+7)%12, (i+9)%12, (i+11)%12] # major scale
    for note in song:
        if note not in scale:
            return False
    return True

main()
