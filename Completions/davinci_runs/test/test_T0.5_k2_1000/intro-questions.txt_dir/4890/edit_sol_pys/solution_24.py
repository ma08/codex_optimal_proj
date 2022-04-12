

def main():
    """
    This function is used to run the program.

    Returns:
        None
    """
    # Read input
    n, m, s, d = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]

    # Calculate the number of cold drinks in the fridge
    cold_drinks_in_fridge = sum(c)

    # If there are more cold drinks than the number of students, then output the empty array
    if cold_drinks_in_fridge >= m:
        print(' '.join([str(0) for i in range(s)]))
        return

    # Calculate the number of empty slots
    empty_slots = s - len(c)

    # Calculate the number of drinks to add to the fridge and the number of drinks to add to each slot
    drinks_to_add_in_fridge = min(n, m - cold_drinks_in_fridge)
    drinks_to_add_per_slot = [0 for i in range(s)]

    # Calculate the number of drinks to add to each slot, if there are more empty slots than drinks to add
    for i in range(s):
        if c[i] < d:
            drinks_to_add_per_slot[i] = min(d - c[i], drinks_to_add_in_fridge)
            drinks_to_add_in_fridge -= drinks_to_add_per_slot[i]

    # If there are still drinks to add, then output "impossible"
    if drinks_to_add_in_fridge > 0:
        print("impossible")
        return

    # Output the drinks to add in each slot
    print(' '.join([str(i) for i in drinks_to_add_per_slot]))

if __name__ == "__main__":
    main()
