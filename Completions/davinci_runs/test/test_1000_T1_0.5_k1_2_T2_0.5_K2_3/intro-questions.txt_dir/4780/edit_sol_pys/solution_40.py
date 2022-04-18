

def main():
    """Ants."""
    num_1 = int(input())
    num_2 = int(input())
    first_row = input()
    second_row = input()
    time = int(input())
    row_1 = []
    row_2 = []
    for i in range(num_1):
        row_1.append(first_row[i])
    for i in range(num_2):
        row_2.append(second_row[i])
    for i in range(time):
        for i in range(min(num_1, num_2)):
            row_1[i], row_2[i] = row_2[i], row_1[i]
    for i in range(num_1):
        print(row_1[i], end=" ")
    for i in range(num_2):
        print(row_2[i], end=" ")

if __name__ == "__main__":
    main()
