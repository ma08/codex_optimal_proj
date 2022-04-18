
import sys, math


notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

def main():
    num_notes = int(sys.stdin.readline().strip())
    song = sys.stdin.readline().strip().split()
    scales = []
    for i in range(12):
        if i == 1:
            scale.append(notes[3])
            scale.append(notes[5])
            scale.append(notes[6])
            scale.append(notes[8])
            scale.append(notes[10])
            scale.append(notes[11])
            scales.append(scale)
            continue
        if i == 3:
            scale.append(notes[5])
            scale.append(notes[7])
            scale.append(notes[8])
            scale.append(notes[10])
            scale.append(notes[0])
            scale.append(notes[1])
            scales.append(scale)
            continue
        if i == 6:
            scale.append(notes[8])
            scale.append(notes[10])
            scale.append(notes[11])
            scale.append(notes[1])
            scale.append(notes[3])
            scale.append(notes[4])
            scales.append(scale)
            continue
        if i == 8:
            scale.append(notes[10])
            scale.append(notes[0])
            scale.append(notes[1])
            scale.append(notes[3])
            scale.append(notes[5])
            scale.append(notes[6])
            scales.append(scale)
            continue
        if i == 10:
            scale.append(notes[0])
            scale.append(notes[2])
            scale.append(notes[3])
            scale.append(notes[5])
            scale.append(notes[7])
            scale.append(notes[8])
            scales.append(scale)
            continue
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
