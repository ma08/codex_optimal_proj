

def main():
    """
    This function is used to run the program.

    Returns:
        None
    """
    # Read input
    n, m, s, d = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]

    # Calculate the number of cold drinks and the number of empty slots
    cold_drinks, empty_slots = sum(c), s - len(c)

    # If there are more cold drinks than the number of students, then output the empty array
    if cold_drinks >= m:
        print(' '.join([str(0) for i in range(s)]))
        return

    # If there are more empty slots than drinks to add, then output the drinks to add in each slot
    if empty_slots >= drinks_to_add:
        print(' '.join([str(1) if i < drinks_to_add else str(0) for i in range(s)]))
        return

if __name__ == "__main__":
    main()
