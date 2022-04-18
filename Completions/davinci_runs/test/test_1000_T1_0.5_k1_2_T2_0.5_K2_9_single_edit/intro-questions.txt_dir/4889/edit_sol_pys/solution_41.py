

def main(steel_rods, rod_lengths):


    rod_lengths.sort()
    total_length = 0

    while len(rod_lengths) > 1:
        total_length += rod_lengths[0] + rod_lengths[1] - 1
        rod_lengths.pop(0)
        rod_lengths.pop(0)
        rod_lengths.append(total_length)
        rod_lengths.sort()
        total_length = 0

    return rod_lengths[0]

if __name__ == "__main__":
    steel_rods = int(input())
    rod_lengths = []

    for _ in range(steel_rods):
        rod_lengths.append(int(input()))

    print(main(steel_rods, rod_lengths))
