
import sys

def main():
    lines = sys.stdin.readlines()

    # Parse the lines
    commands = []
    for line in lines:
        # Split the line
        line = line.strip().split()

        # Parse the command
        if line[0] == "buy":  # buy 10 100
            commands.append(["buy", int(line[1]), int(line[2])])  # ["buy", 10, 100]
        elif line[0] == "sell":  # sell 10 100
            commands.append(["sell", int(line[1]), int(line[2])])  # ["sell", 10, 100]
        elif line[0] == "split":  # split 2
            commands.append(["split", int(line[1])])  # ["split", 2]
        elif line[0] == "merge":  # merge 2
            commands.append(["merge", int(line[1])])  # ["merge", 2]
        elif line[0] == "die":  # die 100
            commands.append(["die", int(line[1])])  # ["die", 100]
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
            total_cost += command[1] * command[2]
        elif command[0] == "sell":
            shares -= command[1]
            total_price += command[1] * command[2]
        elif command[0] == "split":
            shares *= command[1]
            total_cost *= command[1]
        elif command[0] == "merge":
            if shares % command[1] != 0:
                total_price += (shares % command[1]) * (total_cost / shares)
                shares -= (shares % command[1])
            shares //= command[1]
            total_cost //= command[1]
        elif command[0] == "die":
            total_price += shares * command[1]
            total_price -= total_price * 0.3
            break

    print(total_price)

main()
