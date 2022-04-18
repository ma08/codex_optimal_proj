

def main():
    socks, capacity, color_diff = [int(x) for x in input().split()]  # socks - number of socks, capacity - max number of socks in a machine, color_diff - max color difference between two socks in the same machine
    colors = [int(x) for x in input().split()]  # colors of each sock
    colors.sort()  # sort socks by their colors
    num_machines = 0
    current_machine = []  # each machine will have its own list of socks
    for color in colors:
        if not current_machine:  # if the current machine is empty
            current_machine.append(color)
            num_machines += 1
        elif abs(current_machine[-1] - color) <= color_diff and len(current_machine) < capacity:  # if the color difference between the last sock in the current machine and the current sock is smaller than the max color difference and the machine is not full
            current_machine.append(color)
        else:  # if the machine is full or the color difference between the last sock in the current machine and the current sock is greater than the max color difference
            current_machine = [color]
            num_machines += 1
    print(num_machines)

if __name__ == "__main__":
    main()
