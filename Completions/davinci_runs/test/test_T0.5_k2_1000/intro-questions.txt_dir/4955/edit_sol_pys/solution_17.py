
def main():
    n = int(input())
    notes = input().split()
    notes.append(notes[0])  # To avoid index out of range
    scales = []
    for i in range(12):
        scale = [notes[i]]
        for j in range(1, 8):
            if j % 7 == 0:  # Perfect unison
                scale.append(notes[i])
            elif j % 7 == 1 or j % 7 == 2:  # Major second or minor third
                scale.append(notes[i+2])
            else:  # Major third or perfect fourth
                scale.append(notes[i+1])
        if set(notes) <= set(scale):  # Check if notes are in scale
            scales.append(notes[i])
    if scales:
        print(" ".join(scales))
    else:
        print("None")

main()
