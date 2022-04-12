

def main():
    """
    This function is used to run the program.

    Returns:
        None
    """
    # Read input and convert to integers
    n, m, s, d = map(int, input().split())
    c = list(map(int, input().split()))

    # Calculate the number of cold drinks in the fridge
    cold_drinks_in_fridge = sum(c)

    # If there are more cold drinks in the fridge than the number of students, then output the empty list
    if cold_drinks_in_fridge >= m:
        print(' '.join(map(str, [0] * s)))
        return

    # Calculate the number of empty slots
    empty_slots = s - len(c)

    # Calculate the number of drinks to add to the front of the fridge, which is the minimum of the number of drinks
    # in the fridge and the number of students
    drinks_to_add = min(n, m - cold_drinks_in_fridge)

    # If there are more empty slots than drinks to add, then output the drinks to add in each slot
    if empty_slots >= drinks_to_add:
        print(' '.join(map(str, [1 if i < drinks_to_add else 0 for i in range(s)])))
        return

    # Calculate the number of drinks to add to the back of the fridge
    drinks_to_add = max(0, drinks_to_add - empty_slots)

    # Calculate the number of drinks to add to each slot
    drinks_to_add_per_slot = [0] * s
    for i in range(s):
        if c[i] < d:
            drinks_to_add_per_slot[i] = min(d - c[i], drinks_to_add)
            drinks_to_add -= drinks_to_add_per_slot[i]

    # If there are still drinks to add, then output "impossible"
    if drinks_to_add > 0:
        print("impossible")
        return

    # Output the drinks to add in each slot
    print(' '.join(map(str, drinks_to_add_per_slot)))

if __name__ == "__main__":
    main()
