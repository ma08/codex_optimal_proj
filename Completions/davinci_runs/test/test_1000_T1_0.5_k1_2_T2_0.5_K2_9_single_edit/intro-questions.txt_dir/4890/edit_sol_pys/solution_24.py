

def main():
    """
    This function is used to run the program.

    Returns:
        None
    """
    # Read input
    n, m, s, d = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]

    # Calculate the number of cold drinks
    cold_drinks = sum(c)

    # If there are more cold drinks than the number of students, then output the empty list
    if cold_drinks >= m:
        print(' '.join([str(0) for i in range(s)]))
        return

    # Calculate the number of empty positions
    empty_positions = s - len(c)

    # Calculate the number of drinks to add to the front of the fridge (if needed)
    drinks_to_add = min(n, m - cold_drinks)

    # If there are more empty positions than drinks to add, then output the drinks to add in each position
    if empty_positions >= drinks_to_add:
        print(' '.join([str(1) if i < drinks_to_add else str(0) for i in range(s)]))
        return

    # Calculate the number of drinks to add to the back of the fridge (if needed)
    drinks_to_add = max(0, drinks_to_add - empty_positions)

    # Calculate the number of drinks to add to each position
    drinks_to_add_per_position = [0 for i in range(s)]
    for i in range(s):
        if c[i] < d:
            drinks_to_add_per_position[i] = min(d - c[i], drinks_to_add)
            drinks_to_add -= drinks_to_add_per_position[i]

    # If there are still drinks to add, then output "impossible"
    if drinks_to_add > 0:
        print("impossible")
        return

        return

    # Output the drinks to add in each position
    print(' '.join([str(i) for i in drinks_to_add_per_position]))

if __name__ == "__main__":
    main()
