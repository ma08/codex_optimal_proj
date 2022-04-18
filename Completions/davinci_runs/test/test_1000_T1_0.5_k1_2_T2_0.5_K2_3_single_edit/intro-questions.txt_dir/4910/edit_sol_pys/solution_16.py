
import sys

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
    num_colleagues = int(lines[0])
    costumes = []
    for i in range(1, num_colleagues + 1):
        costumes.append(lines[i])
    costume_counts = {}
    for costume in costumes:
        if costume not in costume_counts:
            costume_counts[costume] = 1
        else:
            costume_counts[costume] += 1
    highest = 0
    for costume in costume_counts:
        if costume_counts[costume] > highest:
            highest = costume_counts[costume]
    best_costumes = []
    for costume in costume_counts:
        if costume_counts[costume] == highest:
            best_costumes.append(costume)
    best_costumes.sort()
    for costume in best_costumes:
        print(costume)

if __name__ == "__main__":
    main()
