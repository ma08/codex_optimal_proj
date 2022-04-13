

def main():
    n = int(input())
    notes = input().split()
    scales = []
    for i in range(12):
        scale = [notes[i]]
        for j in range(1, 8):
            if j % 7 == 0:
                scale.append(notes[i])
            else:
                scale.append(notes[(i+j)%12])
        if set(notes) <= set(scale):
            scales.append(notes[i])
    if scales:
        print(" ".join(scales))
    else:
        print("none")

main()
