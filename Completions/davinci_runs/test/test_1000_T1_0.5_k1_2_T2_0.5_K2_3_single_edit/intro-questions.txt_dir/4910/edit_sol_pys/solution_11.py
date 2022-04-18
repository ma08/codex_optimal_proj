

import sys

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
    num_colleagues = int(lines[0])
    costumes = []
    for i in range(1, num_colleagues + 1):
        costumes.append(int(lines[i]))
    costume_dict = {}
    for costume in costumes:
        if costumes[costume] not in costume_dict:
            costume_dict[costumes[costume]] = 1
        else:
            costume_dict[costumes[costume]] += 1
    highest = 0
    for costume in costumes:
        if costume_dict[costumes[costume]] > highest:
            highest = costume_dict[costumes[costume]]
    best_costumes = []
    for costume in costumes:
        if costume_dict[costumes[costume]] == highest:
            best_costumes.append(costumes[costume])
    best_costumes.sort()
    for costume in costumes:
        print(costumes[costume])

if __name__ == "__main__":
    main()
