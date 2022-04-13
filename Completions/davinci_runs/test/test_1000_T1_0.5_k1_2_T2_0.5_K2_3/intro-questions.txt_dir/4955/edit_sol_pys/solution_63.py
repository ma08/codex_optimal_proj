

def main():
    n = int(input())
    notes[0] = notes[0][0].upper() + notes[0][1:]
    for i in range(1, len(notes)):
        notes[i] = notes[i][0].lower() + notes[i][1:]
    notes = input().split()
    notes.append(notes[0])
    scales = []
    for i in range(12):
        scale = [notes[i]]
        for j in range(1, 8):
            if j % 7 == 0 or j % 7 == 3 or j % 7 == 4:
                scale.append(notes[i])
            elif j % 7 == 1 or j % 7 == 5:
                scale.append(notes[i+2])
            else:
                scale.append(notes[i+1])
        if set(notes) <= set(scale):
            scales.append(notes[i])
    if scales:
        print(" ".join(scales))
    else:
        print("None")

main()
