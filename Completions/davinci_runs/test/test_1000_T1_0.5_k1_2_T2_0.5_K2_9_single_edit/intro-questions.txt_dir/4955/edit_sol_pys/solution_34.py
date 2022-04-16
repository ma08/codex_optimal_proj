

import sys
all_scales = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


def main():
    n = int(sys.stdin.readline())
    song = sys.stdin.readline().split()
    scales = []
    for scale in all_scales:
        if check_scale(scale, song):
            scales.append(scale)
    if len(scales) == 0:
        print("none")
    else:
        print(" ".join(scales))
    
def check_scale(scale, song):
    scale_index = all_scales.index(scale)
    for i in range(len(song)):
        if song[i] != all_scales[scale_index]:
            return False
        if i % 7 == 0:
            scale_index += 2
        elif i % 7 == 2 or i % 7 == 6:
            scale_index += 1
        scale_index = scale_index % 12
    return True

if __name__ == "__main__":
    main()
