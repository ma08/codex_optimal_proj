# Accepts 10 inputs and outputs the number of distinct numbers modulo 42.
def main():
    # Dictionary to store the modulo values.
    mod = {}
    # Loop through 10 inputs.
    for i in range(10):
        # Store the modulo of the input.
        mod[i] = int(input()) % 42
    # Output the number of distinct modulo values.
    print(len(set(mod.values())))

main()
