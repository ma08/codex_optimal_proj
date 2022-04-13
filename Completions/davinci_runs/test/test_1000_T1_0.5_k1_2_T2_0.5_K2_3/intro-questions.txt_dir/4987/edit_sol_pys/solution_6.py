

def main():
    socks, capacity, color_diff = [int(x) for x in input().split()]
    colors = [int(x) for x in input().split()]
    colors.sort()  # sort socks by their colors
    num_machines = 0
    current_machine = []
    for color in colors:
        if not current_machine:
            current_machine.append(color)
            num_machines += 1
        elif abs(current_machine[-1] - color) <= color_diff and len(current_machine) < capacity:
            current_machine.append(color)
        else:
            current_machine = [color]
            num_machines += 1
    print(num_machines)

if __name__ == "__main__":
    main()
