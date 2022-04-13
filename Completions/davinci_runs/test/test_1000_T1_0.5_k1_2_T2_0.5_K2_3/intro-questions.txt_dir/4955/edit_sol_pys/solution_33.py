
import sys

def main():
    n = int(sys.stdin.readline())
    song = list(sys.stdin.readline().split())
    all_scales = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    scales = []
    for scale in all_scales:
        if check_scale(song, scale, all_scales):
            scales.append(scale)
    if len(scales) == 0:
        print("none")
    else:
        print(" ".join(scales))
    
def check_scale(song, scale, all_scales):
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
