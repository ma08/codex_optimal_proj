

def main():
    """Ants."""
    num_1 = int(input())
    num_2 = int(input())
    first_row = input()
    second_row = input()
    time = int(input())
    row_1 = []
    row_3 = []
    row_2 = []
    for i in range(num_1):
        row_1.append(first_row[i])
    for i in range(num_2):
    for i in range(num_1):
        row_3.append(first_row[i])
        row_2.append(second_row[i])
    for i in range(time):
        for i in range(len(row_1)):
            row_3[i], row_2[i] = row_2[i], row_3[i]
    for i in range(num_1):
        print(row_3[i], end="")
    for i in range(num_2):
        print(row_2[i], end="")

if __name__ == "__main__":
    main()
