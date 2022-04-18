

def main():
    graph = {}
    for _ in range(int(input())):
        line = input().split()
        if line[0] not in graph:
            graph[line[0]] = []
        graph[line[0]].append(line[1])
    print(graph)
    # colors.sort()
    # num_machines = 0
    # current_machine = []
    # for color in colors:
    #     if not current_machine:
    #         current_machine.append(color)
    #         num_machines += 1
    #     elif abs(current_machine[-1] - color) <= color_diff and len(current_machine) < capacity:
    #         current_machine.append(color)
    #     else:
    #         current_machine = [color]
    #         num_machines += 1
    # print(num_machines)

if __name__ == "__main__":
    main()
