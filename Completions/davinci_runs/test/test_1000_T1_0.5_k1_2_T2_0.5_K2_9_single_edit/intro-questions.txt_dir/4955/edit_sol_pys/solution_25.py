

def main():
    n = int(input())
    notes = input().split()
    scales = []
    for i in range(n):
        scale = [notes[i]]
        for j in range(1, 8):
            if j % 7 == 0 or j % 7 == 1 or j % 7 == 2:
                if i + 2 < n:
                    scale.append(notes[i+2])
                else:
                    scale.append(notes[i+2-n])
            else:
                if i + 1 < n:
                    scale.append(notes[i+1])
                else:
                    scale.append(notes[i+1-n])
        if set(notes) <= set(scale):
            scales.append(notes[i])
    if scales:
        print(" ".join(scales))
    else:
        print("none")

main()
