

def main():
    n = int(input())
    notes = input().split()
    notes.append(notes[0])  # Add the first note to the end of the list so that
                            # we can easily use the modulus operator
    scales = []
    for i in range(12):
        scale = [notes[i]]
        for j in range(1, 8):
            if j % 7 == 0:  # A perfect octave
                scale.append(notes[i])
            elif j % 7 == 1 or j % 7 == 2:  # The major second and third
                scale.append(notes[i+2])
            else:  # The minor second, fourth, fifth, and sixth
                scale.append(notes[i+1])
        if set(notes) <= set(scale):
            scales.append(notes[i])
    if scales:
        print(" ".join(scales))
    else:
        print("None")

main()
