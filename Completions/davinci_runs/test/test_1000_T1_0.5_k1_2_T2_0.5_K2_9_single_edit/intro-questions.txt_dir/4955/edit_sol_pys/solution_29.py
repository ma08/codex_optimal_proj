
def main():
    n = int(input())
    notes = input().split()
    notes.append(notes[0])  # to avoid index out of range
    scales = []
    for i in range(12):
        scale = [notes[i]]
        for j in range(1, 8):
            scale.append(notes[i + (j % 7) // 2])
        if set(notes) <= set(scale):
            scales.append(notes[i])
    if scales:
        print(" ".join(scales))
    else:
        print("none")

main()
