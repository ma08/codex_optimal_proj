

def main():
    socks, capacity, color_diff = [int(x) for x in input().split()] #socks is the number of socks, capacity is the number of socks a machine can hold, and color_diff is the maximum difference between colors that can be in the same machine
    colors = [int(x) for x in input().split()] # colors is the list of colors
    colors.sort()
    num_machines = 0 # the number of machines that will be needed
    current_machine = [] # the current machine
    for color in colors:
        if not current_machine: #if the current machine is empty
            current_machine.append(color)
            num_machines += 1
        elif abs(current_machine[-1] - color) <= color_diff and len(current_machine) < capacity: #if the current machine is not empty and the difference between the last color of the current machine and the current color is less than or equal to the maximum difference and the length of the current machine is less than the capacity
            current_machine.append(color)
        else: #if the current machine is not empty and the difference between the last color of the current machine and the current color is greater than the maximum difference or the length of the current machine is greater than the capacity
            current_machine = [color]
            num_machines += 1
    print(num_machines)

if __name__ == "__main__":
    main()
