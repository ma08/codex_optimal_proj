

def main():
    """Ant"""
    input_ant1 = input()
    input_ant2 = input()
    input_time = int(input())
    if input_time % 2 == 0:
        print(input_ant1 + " " + input_ant2)
    else:
        print(input_ant2 + " " + input_ant1)

if __name__ == "__main__":
    main()
