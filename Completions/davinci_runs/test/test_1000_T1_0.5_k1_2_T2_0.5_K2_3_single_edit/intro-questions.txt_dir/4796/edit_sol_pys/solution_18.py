

def main():
    # Read the input
    num_students = int(input())
    # Compute the results
    num_positive = 0
    num_negative = 0
    num_zero = 0
    for i in range(num_students):
        grade = int(input())
        if grade > 0:
            num_positive += 1
        elif grade < 0:
            num_negative += 1
        else:
            num_zero += 1
    # Output the results
    print(round(num_positive / num_students, 3))
    print(round(num_negative / num_students, 3))
    print(round(num_zero / num_students, 3))

if __name__ == '__main__':
    main()
