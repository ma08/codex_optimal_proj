

def main():
    """
    Write a program to find the number of years.
    """
    # input_n = input()
    # input_n = input_n.split(" ")
    # input_n = list(map(int, input_n))
    # input_n = input_n[0]
    # input_n_2 = input_n[1]
    input_n = 4
    input_n_2 = 2
    # input_n_3 = input()
    # input_n_3 = input_n_3.split(" ")
    # input_n_3 = list(map(int, input_n_3))
    input_n_3 = [3, 3, 3, 2]
    count_1 = 0
    for i in range(input_n):
        if input_n_3[i] > input_n_2:
            count_1 += 1
        else:
            break
    if count_1 != 0:
        print("It hadn't snowed this early in", count_1-1, "years!")
    else:
        print("It had never snowed this early!")

if __name__ == '__main__':
    main()