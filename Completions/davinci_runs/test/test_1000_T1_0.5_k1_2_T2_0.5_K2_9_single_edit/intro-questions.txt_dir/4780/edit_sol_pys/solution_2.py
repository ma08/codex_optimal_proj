

def main():
    """
    Main function
    """

    # Get the number of ants in the first and second rows
    num_ants_in_first_row, num_ants_in_second_row = map(int, input().split())

    # Get the order of ants in the first and second rows, respectively
    order_ants_in_first_row = input()
    order_ants_in_second_row = input()

    # Get the number of seconds
    num_seconds = int(input())

    # Initialize the order of ants
    order_ants = ""

    # If the number of seconds is odd, reverse the order of the ants
    if num_seconds % 2 == 1:
        order_ants_in_first_row = order_ants_in_first_row[::-1]
        order_ants_in_second_row = order_ants_in_second_row[::-1]

    # Get the number of ants that will be affected by the explosion
    num_ants_affected = min(num_ants_in_first_row, num_ants_in_second_row)

    for i in range(num_ants_affected):
        order_ants += order_ants_in_first_row[i]
        order_ants += order_ants_in_second_row[i]

    # If there are remaining ants in the first row, add them to the order of ants
    for i in range(num_ants_affected, num_ants_in_first_row):
        order_ants += order_ants_in_first_row[i]

    # If there are remaining ants in the second row, add them to the order of ants
    for i in range(num_ants_affected, num_ants_in_second_row):
        order_ants += order_ants_in_second_row[i]

    # Print the order of ants
    print(order_ants)

if __name__ == "__main__":
    main()
