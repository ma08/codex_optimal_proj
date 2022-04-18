

def main():
    n = int(input())
    notes = []
    for i in range(n-1):
        notes.append(input())
    notes.append(notes[0]) # to make a circle
    scales = []
    for i in range(12):
        scale = []
        for j in range(1, 8):
            if j % 7 == 0 or j % 7 == 1:
                scale.append(notes[i])
            elif j % 7 == 2 or j % 7 == 3:
            elif j % 7 == 4 or j % 7 == 5:
                scale.append(notes[i+3])
                scale.append(notes[i+2])
            else:
                scale.append(notes[i+1])
        if set(notes) <= set(scale):
            scales.append(notes[i])
    if scales:
        print(" ".join(scales))
    else:
        print("none")

main()
