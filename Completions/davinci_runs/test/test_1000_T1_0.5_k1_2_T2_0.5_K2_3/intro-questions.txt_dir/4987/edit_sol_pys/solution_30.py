

def main():
    socks, capacity, color_difference = [int(x) for x in input().split()] # read input
    colors = [int(x) for x in input().split()]
    colors.sort() # sort colors
    num_machines = 0
    current_machine = []
    for color in colors:
        if not current_machine:
            current_machine.append(color)
            num_machines += 1
        elif abs(current_machine[-1] - color) <= color_difference and len(current_machine) < capacity: # check if color is compatible with last color in current machine
            current_machine.append(color)
        else: # if not compatible, create new machine
            current_machine = [color]
            num_machines += 1
    print(num_machines)

if __name__ == "__main__":
    main()
