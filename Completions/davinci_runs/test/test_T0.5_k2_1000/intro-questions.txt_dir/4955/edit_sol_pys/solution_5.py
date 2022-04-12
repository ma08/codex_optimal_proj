

def main():
    n = int(input())
    notes = input().split()[:n]
    notes.append(notes[0])
    scales = []
    for i in range(12):
        scale = [notes[i]]
        for j in range(1, 8):
            if j % 7 == 0:
                scale.append(notes[i])
            elif j % 7 == 1 or j % 7 == 2:
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
