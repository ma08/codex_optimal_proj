

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

    # If there are more cold drinks than the number of students, then output the empty array
    if cold_drinks >= n:
        print(' '.join([str(0) for i in range(s)]))
        return

    # Calculate the number of empty slots
    empty_slots = s - len(c)

    # Calculate the number of drinks to add to the front of the fridge
    drinks_to_add = min(m - cold_drinks, n - cold_drinks)

    # If there are more empty slots than drinks to add, then output the drinks to add in each slot
    if empty_slots >= drinks_to_add:
        print(' '.join([str(1) if i < drinks_to_add else str(0) for i in range(s)]))
        return

    # Calculate the number of drinks to add to the back of the fridge
    drinks_to_add = max(0, drinks_to_add - empty_slots)

    # Calculate the number of drinks to add to each slot
    drinks_to_add_per_slot = [0 for i in range(s)]
    for i in range(s):
        if c[i] < d:
            drinks_to_add_per_slot[i] = min(d - c[i], drinks_to_add)
            drinks_to_add -= drinks_to_add_per_slot[i]

    # If there are still drinks to add, then output "impossible"
    if drinks_to_add > 0:
        print("impossible")
        return

    # Output the drinks to add in each slot
    print(' '.join([str(i) for i in drinks_to_add_per_slot]))

if __name__ == "__main__":
    main()
