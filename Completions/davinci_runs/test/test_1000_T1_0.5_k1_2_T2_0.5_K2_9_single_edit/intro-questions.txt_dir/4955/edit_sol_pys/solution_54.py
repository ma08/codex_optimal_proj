
import sys
notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

def main():
    num_notes = int(sys.stdin.readline().strip())
    song = sys.stdin.readline().strip().split()
    scales = []
    for i in range(12):
        scale = [notes[i]]
        for j in range(1, 8):
            if j % 2 == 0:
                scale.append(notes[(i + 2 * j) % 12])
            else:
                scale.append(notes[(i + 2 * j - 1) % 12])
        scales.append(scale)
    fits = []
    for scale in scales:
        fit = True
        for note in song:
            if note not in scale:
                fit = False
                break
        if fit:
            fits.append(scale[0])
    fits.sort()
    if len(fits) == 0:
        print("none")
    else:
        print(" ".join(fits))
main()
