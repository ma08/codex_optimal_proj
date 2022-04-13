

def main():
    capacity, color_diff = [int(x) for x in input().split()]
    sock_colors = [int(x) for x in input().split()]
    sock_colors.sort()
    num_of_machines = 0
    current_machine_capacity = []
    for sock_color in sock_colors:
        if not current_machine_capacity:
            current_machine_capacity.append(sock_color)
            num_of_machines += 1
        elif abs(current_machine_capacity[-1] - sock_color) <= color_diff and len(current_machine_capacity) < capacity:
            current_machine_capacity.append(sock_color)
        elif abs(current_machine_capacity[-1] - sock_color) > color_diff:
            current_machine_capacity = [sock_color]
            num_of_machines += 1
    print(num_of_machines)

if __name__ == "__main__":
    main()
