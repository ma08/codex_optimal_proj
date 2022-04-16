

import sys

def main():
    lines = sys.stdin.readlines()

    # Parse the lines
    commands = []
    for line in lines:
        # Split the line
        line = line.strip().split()

        # Parse the command
        if line[0] == "buy":
            commands.append(["buy", int(line[1]), float(line[2])])
        elif line[0] == "sell":
            commands.append(["sell", int(line[1]), float(line[2])])
        elif line[0] == "split":
            commands.append(["split", int(line[1])])
        elif line[0] == "merge":
            commands.append(["merge", int(line[1])])
        elif line[0] == "die":
            commands.append(["die", float(line[1])])
        else:
            print("Error: Invalid command")
            return

    # Process the commands
    shares = 0
    total_cost = 0
    total_price = 0
    for command in commands:
        if command[0] == "buy":
            shares += command[1]
            total_cost += command[1] * command[2] * 100
        elif command[0] == "sell":
            shares -= command[1]
            total_price += command[1] * command[2] * 100
        elif command[0] == "split":
            shares *= command[1]
            total_cost *= command[1]
        elif command[0] == "merge":
            if shares % command[1] != 0:
                total_price += (shares % command[1]) * (total_cost / shares) * 100
                shares -= (shares % command[1])
            shares //= command[1]
            total_cost //= command[1]
        elif command[0] == "die":
            total_price += shares * command[1] * 100
            total_price -= total_price * 0.3
            break

    print(round(total_price / 100))

main()
