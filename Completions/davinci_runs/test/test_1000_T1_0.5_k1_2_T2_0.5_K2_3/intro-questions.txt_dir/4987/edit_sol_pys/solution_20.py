

def main():
    socks, capacity, color_difference = [int(x) for x in input().split()] #socks = number of socks, capacity = capacity of each machine, color_difference = color difference
    colors = [int(x) for x in input().split()]
    colors.sort()
    num_machines = 0
    current_machine = []
    for color in colors:
        if not current_machine:
            current_machine.append(color)
            num_machines += 1
        elif abs(current_machine[-1] - color) <= color_difference and len(current_machine) < capacity: #if color difference is less than or equal to the max color difference and machine is not full
            current_machine.append(color)
        else:
            current_machine = [color]
            num_machines += 1
    print(num_machines)

if __name__ == "__main__":
    main()
