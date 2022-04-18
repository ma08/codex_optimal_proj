

import sys

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
    num_colleagues = int(lines[0])
    outfits = []
    for i in range(1, num_colleagues + 1):
        outfits.append(lines[i])
    outfits_dict = {}
    for outfit in outfits:
        if outfit not in outfits_dict:
            outfits_dict[outfit] = 1
        else:
            outfits_dict[outfit] += 1
    highest = 0
    for outfit in outfits_dict:
        if outfits_dict[outfit] > highest:
            highest = outfits_dict[outfit]
    best_costumes = []
    for outfit in outfits_dict:
        if outfits_dict[outfit] == highest:
            best_costumes.append(outfit)
    best_costumes.sort()
    for costume in best_costumes:
        print(costume)

if __name__ == "__main__":
    main()
