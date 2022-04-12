import sys

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]  # all possible notes

def main():
    num_notes = int(sys.stdin.readline().strip())  # number of notes in song
    song = sys.stdin.readline().strip().split()
    scales = []  # list of all possible scales
    for i in range(12):
        scale = [notes[i]]  # first note of scale
        for j in range(1, 8):
            if j % 2 == 0:
                scale.append(notes[(i + 2 * j) % 12])  # add note 2j steps away
            else:
                scale.append(notes[(i + 2 * j - 1) % 12])  # add note 2j-1 steps away
        scales.append(scale)
    fits = []  # list of scales that fit the song
    for scale in scales:
        fit = True  # if all notes in song are in the scale, fit is true
        for note in song:
            if note not in scale:
                fit = False  # if one note is not in the scale, fit is false
                break
        if fit:
            fits.append(scale[0])  # add the first note of the scale to the list of fits
    fits.sort()  # sort the list of fits alphabetically
    if len(fits) == 0:
        print("none")  # if no scales fit the song, print none
    else:
        print(" ".join(fits))  # otherwise, print the list of fits


main()  # run the program
