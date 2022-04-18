

def main():
    socks, capacity, color_diff = [int(x) for x in input().split()]  # socks - number of socks, capacity - max number of socks in a machine, color_diff - max color difference between two socks in a machine
    colors = [int(x) for x in input().split()]  # colors of each sock
    colors.sort()  # sort socks by their colors
    num_machines = 0
    current_machine = []  # each machine will have its own list of socks
    for color in colors:
        if not current_machine:  # if the current machine is empty
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
