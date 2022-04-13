


def reverse_bin(input_string):
    return int(bin(int(input_string, 2))[2:][::-1], 2)

print(reverse_bin(input("Enter number: ")))
