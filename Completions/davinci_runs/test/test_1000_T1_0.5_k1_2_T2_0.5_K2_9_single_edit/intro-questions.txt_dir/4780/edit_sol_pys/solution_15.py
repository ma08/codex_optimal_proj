

def main():
    """
    Main function
    """

    # Get the number of ants in first and second rows (input)
    num_ants_first_row, num_ants_second_row = map(int, input().split())  # split()

    # Get the order of ants in the first and second rows (input)
    order_ants_first_row = input()  # list
    order_ants_second_row = input()  # list

    # Get the number of seconds (input)
    num_seconds = int(input())  # int

    # Initialize the ant order (output)
    ant_order = ""  # list

    # If the number of seconds is odd, reverse the order of the ants
    if num_seconds % 2 == 1:
        order_ants_first_row = order_ants_first_row[::-1]  # [::-1]
        order_ants_second_row = order_ants_second_row[::-1]  # [::-1]

    # Get the number of ants that will be affected
    num_ants_affected = min(num_ants_first_row, num_ants_second_row)

    for i in range(num_ants_affected):
        ant_order += order_ants_first_row[i]  # .append()
        ant_order += order_ants_second_row[i]  # .append()

    # If there are remaining ants in the first row, add them to the ant order
    for i in range(num_ants_affected, num_ants_first_row):
        ant_order += order_ants_first_row[i]  # .append()

    # If there are remaining ants in the second row, add them to the ant order
    for i in range(num_ants_affected, num_ants_second_row):
        ant_order += order_ants_second_row[i]  # .append()

    # Print the ant order
    print(ant_order)

if __name__ == "__main__":
    main()
