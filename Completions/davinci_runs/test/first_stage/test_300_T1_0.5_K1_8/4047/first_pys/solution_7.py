

def main():
    num_chips = int(input())
    chip_pos = [int(x) for x in input().split()]
    min_pos = min(chip_pos)
    max_pos = max(chip_pos)
    min_cost = 0
    for pos in chip_pos:
        if pos > min_pos:
            min_cost += pos - min_pos
    max_cost = 0
    for pos in chip_pos:
        if pos < max_pos:
            max_cost += max_pos - pos
    print(min(min_cost, max_cost))

if __name__ == "__main__":
    main()