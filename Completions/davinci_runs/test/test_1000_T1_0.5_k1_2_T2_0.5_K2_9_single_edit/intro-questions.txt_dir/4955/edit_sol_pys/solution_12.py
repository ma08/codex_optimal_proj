

def main():
    n = int(input())
    notes = input().split() + [notes[0]]
    scales = []
    for i in range(12):
        scale = [notes[i]]
        for j in range(1, 8):
            scale.append(notes[i + (j-1) % 7])
        if set(notes) <= set(scale):
            scales.append(notes[i])
    if scales:
        print(" ".join(scales))
    else:
        print("invalid")

main()
