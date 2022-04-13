
import sys

def main():
    try:
        lines = []
        for line in sys.stdin:
            lines.append(line.rstrip('\n'))
        num_colleagues = int(lines[0])
        costumes_list = []
        for i in range(1, num_colleagues + 1):
            costumes_list.append(lines[i])
        costume_dict = {}
        for costume in costumes_list:
            if costume not in costume_dict:
                costume_dict[costume] = 1
            else:
                costume_dict[costume] += 1
        highest = 0
        for costume in costume_dict:
            if costume_dict[costume] > highest:
                highest = costume_dict[costume]
        best_costumes = []
        for costume in costume_dict:
            if costume_dict[costume] == highest:
                best_costumes.append(costume)
        best_costumes.sort()
        for costume in best_costumes:
            print(costume)
    except:
        print("INVALID INPUT")

if __name__ == "__main__":
    main()
