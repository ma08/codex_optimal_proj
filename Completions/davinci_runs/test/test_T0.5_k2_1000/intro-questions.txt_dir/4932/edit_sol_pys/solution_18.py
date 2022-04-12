

def main():
    """
    Read the input and output the expected result.
    """
    a, b, c, d = [int(i) for i in input().split()]
    p, m, g = [int(i) for i in input().split()]
    #print(a, b, c, d, p, m, g)

    # Aggressive dog A
    aggressive_dog_a_start = 0
    aggressive_dog_a_end = a
    # Aggressive dog B
    aggressive_dog_b_start = c
    aggressive_dog_b_end = c + d
    #print(aggressive_dog_a_start, aggressive_dog_a_end, aggressive_dog_b_start, aggressive_dog_b_end)

    # Check if the postman is attacked by both dogs
    if (p >= aggressive_dog_a_start and p <= aggressive_dog_a_end) \
            and (p >= aggressive_dog_b_start and p <= aggressive_dog_b_end):
        print("both")
    # Check if the postman is attacked by one dog
    elif (p >= aggressive_dog_a_start and p <= aggressive_dog_a_end) \
            or (p >= aggressive_dog_b_start and p <= aggressive_dog_b_end):
        print("one")
    # Check if the postman is attacked by none of the dogs
    else:
        print("none")

    # Check if the milkman is attacked by both dogs
    if (m >= aggressive_dog_a_start and m <= aggressive_dog_a_end) \
            and (m >= aggressive_dog_b_start and m <= aggressive_dog_b_end):
        print("both")
    # Check if the milkman is attacked by one dog
    elif (m >= aggressive_dog_a_start and m <= aggressive_dog_a_end) \
            or (m >= aggressive_dog_b_start and m <= aggressive_dog_b_end):
        print("one")
    # Check if the milkman is attacked by none of the dogs
    else:
        print("none")

    # Check if the garbage man is attacked by both dogs
    if (g >= aggressive_dog_a_start and g <= aggressive_dog_a_end) \
            and (g >= aggressive_dog_b_start and g <= aggressive_dog_b_end):
        print("both")
    # Check if the garbage man is attacked by one dog
    elif (g >= aggressive_dog_a_start and g <= aggressive_dog_a_end) \
            or (g >= aggressive_dog_b_start and g <= aggressive_dog_b_end):
        print("one")
    # Check if the garbage man is attacked by none of the dogs
    else:
        print("none")

if __name__ == "__main__":
    main()
