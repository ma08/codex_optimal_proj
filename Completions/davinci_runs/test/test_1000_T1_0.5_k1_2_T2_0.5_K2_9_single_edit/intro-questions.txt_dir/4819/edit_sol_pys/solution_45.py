

# Accepts 5 inputs and outputs the number of distinct numbers modulo 42
def main():
    # Dictionary to store the modulo values
    mod = {}
    for i in range(5):
        # Store the modulo of the input
        mod[i] = int(input()) % 43
    # Output the number of distinct modulo values
    print(len(set(mod.values())))

main()
