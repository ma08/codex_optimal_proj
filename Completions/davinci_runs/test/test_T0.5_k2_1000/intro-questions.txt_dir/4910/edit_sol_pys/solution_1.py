

import sys

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
    num_colleagues = int(lines[0])
    clothes = []
    for i in range(1, num_colleagues + 1):
        clothes.append(lines[i])
    clothes_dict = {}
    for clothes in clothes:
        if clothes not in clothes_dict:
            clothes_dict[clothes] = 1
        else:
            clothes_dict[clothes] += 1
    highest = 0
    for clothes in clothes_dict:
        if clothes_dict[clothes] > highest:
            highest = clothes_dict[clothes]
    best_clothes = []
    for clothes in clothes_dict:
        if clothes_dict[clothes] == highest:
            best_clothes.append(clothes)
    best_clothes.sort()
    for clothes in best_clothes:
        print(clothes)

if __name__ == "__main__":
    main()
