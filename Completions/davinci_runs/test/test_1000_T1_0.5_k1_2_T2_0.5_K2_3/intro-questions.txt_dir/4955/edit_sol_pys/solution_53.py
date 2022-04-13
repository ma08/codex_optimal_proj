

import sys

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'] 

def main():
    n = int(sys.stdin.readline().strip())
    song = sys.stdin.readline().strip().split()
    song = [notes.index(x) for x in song]
    scales = []
    for i in range(12):
        if valid(i, song):
            scales.append(i)
    if len(scales) == 0:
        print("none")
    else:
        print(' '.join([notes[x] for x in scales]))

def valid(i, song):
    scale = [i, (i+2)%12, (i+4)%12, (i+5)%12, (i+7)%12, (i+9)%12, (i+11)%12]
    for note in song:
        if note not in scale:
            return False
    return True

main()
